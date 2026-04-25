import sys
import os
import chromadb
from chromadb.utils import embedding_functions
import uuid

# Add project root to sys.path to allow importing config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class NexusVectorStore:
    """
    A wrapper for ChromaDB to store and retrieve cross-domain insights.
    
    Attributes:
        client (PersistentClient): The ChromaDB client.
        embedding_fn (SentenceTransformerEmbeddingFunction): The embedding function.
        collection (Collection): The ChromaDB collection.
    """
    def __init__(self, collection_name: str = config.CHROMA_COLLECTION):
        """
        Initializes the vector store with a specific collection name.
        """
        self.client = chromadb.PersistentClient(path="./nexus_db")
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=config.EMBEDDING_MODEL
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn
        )

    def add_insight(self, domain: str, problem: str, solution: str, metadata: dict = None):
        """
        Adds a domain-specific insight to the vector store.
        
        Args:
            domain (str): The domain name.
            problem (str): The structural problem.
            solution (str): The mechanism or solution.
            metadata (dict, optional): Additional metadata.
        """
        if metadata is None:
            metadata = {}
            
        metadata.update({
            "domain": domain,
            "problem_type": metadata.get("problem_type", "general")
        })
        
        content = f"Domain: {domain} | Problem: {problem} | Solution: {solution}"
        
        self.collection.add(
            documents=[content],
            metadatas=[metadata],
            ids=[str(uuid.uuid4())]
        )

    def find_similar_solutions(self, query: str, n_results: int = 5) -> list:
        """
        Searches for solutions that are semantically similar to the query.
        
        Args:
            query (str): The search query.
            n_results (int): Number of results to return.
            
        Returns:
            list: A list of matched insights.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        formatted_results = []
        if results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                formatted_results.append({
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if "distances" in results else None
                })
        return formatted_results

    def clear(self):
        """
        Resets the collection by deleting all entries.
        """
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            embedding_function=self.embedding_fn
        )

if __name__ == "__main__":
    # Test Vector Store
    store = NexusVectorStore()
    store.add_insight(
        "Epidemiology", 
        "Contagion propagation in dense networks", 
        "Dynamic contact tracing and isolation",
        {"problem_type": "propagation"}
    )
    
    similar = store.find_similar_solutions("How to stop information spreading in a social network?")
    print(f"Found {len(similar)} similar solutions.")
    for s in similar:
        print(f"-> {s['content']}")
