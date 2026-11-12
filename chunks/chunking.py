
text = """
Machine Learning is a field of Artificial Intelligence.
It allows computers to learn from data.
Supervised learning uses labelled data.
Unsupervised learning identifies patterns in unlabelled data.
Deep learning uses neural networks.
"""

chunk_size = 100
overlap = 20

start = 0
chunks = []

while start < len(text):

    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start = end - overlap

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}:")
    print(chunk)
