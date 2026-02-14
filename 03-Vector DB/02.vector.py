from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.http.models import PointStruct

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example texts to embed
texts = ["This is a sample text", "Another example of text"]

# Generate embeddings
embeddings = model.encode(texts)

# Print the shape of the embeddings instead of the full arrays
print("Embeddings shape:", embeddings.shape)
print("First embedding:", embeddings[0])



client = QdrantClient(url="http://localhost:6333")



client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=384, distance=Distance.DOT),
)


## insert data : 

points = [
    PointStruct(
        id=i + 1,  # Assign a unique ID to each point
        vector=embedding.tolist()  # Convert embedding to a list for insertion
    )
    for i, embedding in enumerate(embeddings)  # Loop through embeddings and create PointStruct
]

client.upsert(
    collection_name="test_collection",
    points=points  # Insert all points into the collection
)