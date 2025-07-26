import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL"))

def summarise_cluster(cluster_lines):
    prompt = f"""
    Summarise these log lines into a concise operational description.

    If any line indicates an error, failure, timeout, or permission denial, clearly mention it.
    Do not suggest solutions. Only summarise the logs concisely.

    {cluster_lines}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def suggest_root_cause(anomaly_line):
    prompt = f"""
     The following log line indicates an anomaly.

    List 1-3 **operationally plausible** root cause hypotheses, based only on this log and general production knowledge. Avoid assumptions unrelated to the log content. Do not suggest solutions.

    Log line:
    {anomaly_line}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
