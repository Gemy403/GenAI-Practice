from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example texts to embed
texts = ["This is a sample text", "Another example of text"]

# Generate embeddings
embeddings = model.encode(texts)

# Print the shape of the embeddings instead of the full arrays
print("Embeddings shape:", embeddings.shape)
print("First embedding:", embeddings[0])