from sklearn.cluster import DBSCAN

def cluster_embeddings(embeddings, eps=0.2, min_samples=1):
    clustering = DBSCAN(eps=eps, min_samples=min_samples, metric='cosine').fit(embeddings)
    return clustering.labels_
