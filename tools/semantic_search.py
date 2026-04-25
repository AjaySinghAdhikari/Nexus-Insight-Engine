import sys
import os
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Add project root to sys.path to allow importing config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class SemanticSearcher:
    """
    A tool for semantic similarity and text encoding using sentence-transformers.
    
    Attributes:
        model (SentenceTransformer): The underlying embedding model.
    """
    def __init__(self, model_name: str = config.EMBEDDING_MODEL):
        """
        Initializes the searcher with a specific model.
        """
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str) -> np.ndarray:
        """
        Encodes text into a vector embedding.
        
        Args:
            text (str): Input text.
            
        Returns:
            np.ndarray: The resulting vector.
        """
        return self.model.encode(text)

    def similarity(self, text1: str, text2: str) -> float:
        """
        Calculates cosine similarity between two pieces of text.
        
        Args:
            text1 (str): First text.
            text2 (str): Second text.
            
        Returns:
            float: Cosine similarity score (0.0 to 1.0).
        """
        emb1 = self.model.encode(text1, convert_to_tensor=True)
        emb2 = self.model.encode(text2, convert_to_tensor=True)
        score = util.cos_sim(emb1, emb2).item()
        return max(0.0, min(1.0, float(score)))

    def find_most_similar(self, query: str, candidates: list[str]) -> list[tuple[str, float]]:
        """
        Ranks candidates by semantic similarity to the query.
        
        Args:
            query (str): The search query.
            candidates (list[str]): List of texts to compare against.
            
        Returns:
            list[tuple]: Sorted list of (candidate, score) pairs.
        """
        if not candidates:
            return []
            
        query_emb = self.model.encode(query, convert_to_tensor=True)
        candidate_embs = self.model.encode(candidates, convert_to_tensor=True)
        
        scores = util.cos_sim(query_emb, candidate_embs)[0].tolist()
        
        ranked = list(zip(candidates, scores))
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked

if __name__ == "__main__":
    # Quick test
    searcher = SemanticSearcher()
    query = "How do ants find the shortest path?"
    candidates = [
        "Distributed pathfinding using pheromones",
        "The history of urban architecture",
        "Reinforcement learning in robotic swarms",
        "Quantum entanglement in superconductors"
    ]
    results = searcher.find_most_similar(query, candidates)
    for text, score in results:
        print(f"[{score:.4f}] {text}")
