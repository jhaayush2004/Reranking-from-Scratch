from sentence_transformers import CrossEncoder
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

'''
A cross-encoder is a different type of neural network architecture used in Natural Language Processing (NLP), specifically for sentence or text pair classification. Unlike BM25Okapi which focuses on ranking individual documents, a cross-encoder deals with understanding the relationship between two pieces of text.

Here's how a cross-encoder works:

Takes two texts as input: It receives two sentences or short texts as input.

Encodes the texts: It encodes each sentence into a numerical representation capturing its meaning.

Compares the encodings: It then compares these encodings to determine how similar or related the two pieces of text are. 
This comparison often results in a score between 0 and 1, with a higher score indicating greater similarity.

so, cross-encoder is basically used here for reranking tool as it contains a group of bert based models.
'''

pairs = []
for doc in top_4_documents:
  pairs.append((query,doc))
pairs
'''
[('Natural language processing techniques enhance keyword extraction efficiency.',
  'Efficient keyword extraction enhances search accuracy.'),
 ('Natural language processing techniques enhance keyword extraction efficiency.',
  'Machine learning algorithms can optimize keyword extraction methods.'),
 ('Natural language processing techniques enhance keyword extraction efficiency.',
  'Understanding document structure aids in keyword extraction.'),
 ('Natural language processing techniques enhance keyword extraction efficiency.',
  'Document analysis involves extracting keywords.')]
  '''

scores = cross_encoder.predict(pairs)
scored_docs = zip(scores, top_4_documents)
reranked_doc_cross_encoder = sorted(scored_docs, key=lambda x: x[0], reverse=True)
reranked_doc_cross_encoder
'''
[(3.137871, 'Efficient keyword extraction enhances search accuracy.'),
 (0.8421656,
  'Machine learning algorithms can optimize keyword extraction methods.'),
 (-2.8781917, 'Document analysis involves extracting keywords.'),
 (-2.9193, 'Understanding document structure aids in keyword extraction.')]
'''



