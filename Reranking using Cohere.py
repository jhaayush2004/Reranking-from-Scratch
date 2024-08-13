! pip install cohere
import cohere

co = cohere.Client("XzZzzfBfXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


response = co.rerank(
   model="rerank-english-v3.0",
    query="Natural language processing techniques enhance keyword extraction efficiency.",
    documents=top_4_documents,
    return_documents=True
)
print(response)
'''
id='76f17682-9625XXXXX0-a1fb-5XXXXXXfd' results=[RerankResponseResultsItem(document=RerankResponseResultsItemDocument(text='Efficient keyword extraction enhances search accuracy.'), index=0, relevance_score=0.99411184),
RerankResponseResultsItem(document=RerankResponseResultsItemDocument(text='Machine learning algorithms can optimize keyword extraction methods.'), index=1, relevance_score=0.9129032),
RerankResponseResultsItem(document=RerankResponseResultsItemDocument(text='Understanding document structure aids in keyword extraction.'), index=2, relevance_score=0.32885265), 
RerankResponseResultsItem(document=RerankResponseResultsItemDocument(text='Document analysis involves extracting keywords.'), index=3, relevance_score=0.02865267)] 
meta=ApiMeta(api_version=ApiMetaApiVersion(version='1', is_deprecated=None, is_experimental=None), billed_units=ApiMetaBilledUnits(input_tokens=None, output_tokens=None, search_units=1, classifications=None), 
tokens=None, warnings=None)
'''

#Gives top ranked document
response.results[0].document.text

#gives similarity_score of query& top-ranked document
response.results[0].relevance_score

for i in range(4):
  print(f'text: {response.results[i].document.text} score: {response.results[i].relevance_score}')

'''
text: Efficient keyword extraction enhances search accuracy. score: 0.99411184
text: Machine learning algorithms can optimize keyword extraction methods. score: 0.9129032
text: Understanding document structure aids in keyword extraction. score: 0.32885265
text: Document analysis involves extracting keywords. score: 0.02865267
'''
