!pip install sentence-transformers
from sentence_transformers import SentenceTransformer


# Load pre-trained Sentence Transformer model
model_name = 'sentence-transformers/paraphrase-xlm-r-multilingual-v1'
model = SentenceTransformer(model_name)


document_embeddings = model.encode(documents)
query_embedding = model.encode(query)


#can check document embeddings created for each docs in documents.
for i,embedding in enumerate(document_embeddings):
  print(f"Document {i+1} Embedding: {embedding} ")
  
#can check query embeddings 
print(f"Query Embedding: {query_embedding}")

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(np.array([query_embedding]), document_embeddings)
most_similar_index = np.argmax(similarities)
#get most similar document
most_similar_document = documents[most_similar_index]
# get similarity_score of most similar document
similarity_score = similarities[0][most_similar_index]

sorted_indices = np.argsort(similarities[0])[::-1]
ranked_documents = [(documents[i], similarities[0][i]) for i in sorted_indices]

print("Ranked Documents:")
for rank, (document, similarity) in enumerate(ranked_documents, start=1):
    print(f"Rank {rank}: Document - '{document}', Similarity Score - {similarity}")
'''
Ranked Documents:
Rank 1: Document - 'Efficient keyword extraction enhances search accuracy.', Similarity Score - 0.7521413564682007
Rank 2: Document - 'Machine learning algorithms can optimize keyword extraction methods.', Similarity Score - 0.7448166608810425
Rank 3: Document - 'Understanding document structure aids in keyword extraction.', Similarity Score - 0.6316118240356445
Rank 4: Document - 'Document analysis involves extracting keywords.', Similarity Score - 0.5675694942474365
Rank 5: Document - 'Semantic similarity improves document retrieval performance.', Similarity Score - 0.5503519773483276
Rank 6: Document - 'Keywords are important for keyword-based search.', Similarity Score - 0.458022803068161
Rank 7: Document - 'Keyword-based search relies on sparse embeddings.', Similarity Score - 0.4412330090999603
Rank 8: Document - 'This is a list which containing sample documents.', Similarity Score - 0.16948148608207703
'''
