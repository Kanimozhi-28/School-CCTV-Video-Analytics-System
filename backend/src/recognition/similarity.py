import numpy as np
import face_recognition

def cosine_similarity(embedding1, embedding2):
    # Not strictly needed if using face_recognition.face_distance (which is Euclidean)
    # But useful if we want cosine similarity specifically
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    return dot_product / (norm1 * norm2)

def find_best_match(embedding, database, threshold=0.6):
    """
    Finds the best match for the given embedding in the database.
    database: dict {name: embedding_list}
    threshold: Tolerance for face matching (lower is stricter)
    Returns: (name, distance) or (None, min_dist)
    """
    known_names = list(database.keys())
    known_embeddings = list(database.values())

    if not known_embeddings:
        return None, float('inf')

    # Calculate euclidean distance to all known faces
    # face_recognition uses 128d encodings
    distances = face_recognition.face_distance(known_embeddings, np.array(embedding))
    
    min_dist_index = np.argmin(distances)
    min_dist = distances[min_dist_index]

    if min_dist < threshold:
        return known_names[min_dist_index], min_dist
    
    return "Unknown", min_dist

