!pip install rank_bm25
from rank_bm25 import BM25Okapi
'''Okapi BM25 is a retrieval ranking function commonly used in search engines. 
It assigns a score to each document in a collection based on how relevant it is to a given query.'''

#ranked_documents are those obtained from sentence-transformers model reranking
top_4_documents = [doc[0] for doc in ranked_documents[:4]]

# Tokenizing documents and query
tokenized_top_4_documents = [doc.split() for doc in top_4_documents]
tokenized_query = query.split()

bm25 = BM25Okapi(tokenized_top_4_documents)
bm25_scores = bm25.get_scores(tokenized_query)
bm25_scores
''' array([0.1907998 , 0.16686672, 0.17803252, 0.        ])'''

sorted_indices2 = np.argsort(bm25_scores)[::-1]
reranked_documents = [(top_4_documents[i],bm25_scores[i]) for i in sorted_indices2]
print("Rerank of top 4 Documents:")
for rank, (document, similarity) in enumerate(reranked_documents, start=1):
    print(f"Rank {rank}: Document - '{document}', Similarity Score - {similarity}")
  '''
  Rerank of top 4 Documents:
Rank 1: Document - 'Efficient keyword extraction enhances search accuracy.', Similarity Score - 0.19079979534096053
Rank 2: Document - 'Understanding document structure aids in keyword extraction.', Similarity Score - 0.1780325227902643
Rank 3: Document - 'Machine learning algorithms can optimize keyword extraction methods.', Similarity Score - 0.1668667199671815
Rank 4: Document - 'Document analysis involves extracting keywords.', Similarity Score - 0.0
  '''
