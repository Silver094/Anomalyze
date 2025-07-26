import os
import argparse
from src.reader import read_logs
from src.embedding import generate_embeddings
from src.clustering import cluster_embeddings
from src.summarizer import summarise_cluster, suggest_root_cause

def write_summary(output_path, cluster_summaries, anomalies, include_root_causes):
    with open(output_path, 'w') as f:
        for i, summary in enumerate(cluster_summaries):
            f.write(f"==== Cluster {i+1} Summary ====\n{summary}\n\n")
        f.write("==== Potential Anomalies ====\n")
        if not anomalies:
            f.write("No anomalies detected.\n")
        for anomaly in anomalies:
            f.write(anomaly + "\n")
            if include_root_causes:
                root = suggest_root_cause(anomaly)
                f.write("Possible root causes:\n" + root + "\n\n")
            else:
                f.write("\n")

def main(input_path, output_path, include_root_causes=False):
    if not os.path.exists(input_path):
        print(f"Input file {input_path} does not exist.")
        return
    print("Reading log lines... ")
    log_lines = read_logs(input_path)
    if not log_lines:
        print("No logs found.")
        return
    print("Generating embeddings... ")
    embeddings = generate_embeddings(log_lines)
    if not embeddings:
        print("No embeddings generated.")
        return
    print("Embeddings have been generated successfully.")
    print("Clustering embeddings... ")
    labels = cluster_embeddings(embeddings)
    if labels is None:
        print("Clustering failed.")
        return
    print("Clustering complete. ")
    print("Identifying anomalies and summarizing clusters... ")

    if include_root_causes:
        print("Including root cause hypotheses in the summary.")
    else:
        print("Root cause hypotheses will not be included in the summary.")

    error_keywords = ['error', 'fail', 'denied', 'timeout', 'exception', 'critical']
    clusters, anomalies = {}, []

    for line, label in zip(log_lines, labels):
        if any(k in line.lower() for k in error_keywords):
            anomalies.append(line)
        if label == -1:  # DBSCAN marks noise points with -1
            anomalies.append(line)
        else:
            clusters.setdefault(label, []).append(line)

    print("Summarizing clusters... ")
    cluster_summaries = []
    for cluster_id, lines in clusters.items():
        summary = summarise_cluster("\n".join(lines[:10]))  # limit to first 10 lines for summarisation
        cluster_summaries.append(summary)

    write_summary(output_path, cluster_summaries, anomalies, include_root_causes)
    print(f"Summary written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input log file path")
    parser.add_argument("--output", required=True, help="Output summary file path")
    parser.add_argument("--root-causes", action="store_true", help="Include root cause hypotheses")
    args = parser.parse_args()

    main(args.input, args.output, args.root_causes)
