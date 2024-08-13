# Reranking-from-Scratch
Reranking from scratch using sentence-transformer, BM25, Cohere and Cross-Encoders !!!

# FlashReranking
 Flash Re-ranking (flashreranking) is a technique used in information retrieval systems to improve the relevance of the results presented to users. It involves re-evaluating and re-ordering the top-ranked documents or items retrieved in an initial search or retrieval phase. This process aims to enhance the quality of the results by focusing on a smaller subset of items and applying more sophisticated or computationally intensive ranking methods.

## Reasons for Using Flash Re-ranking
- **Improved Relevance**:

Flash re-ranking allows the system to refine the initial ranking by applying more accurate but computationally expensive algorithms that wouldn't be feasible to apply to the entire corpus.
By focusing on the top k results from the initial retrieval, re-ranking can incorporate more complex features and models to better judge relevance.

- **Combining Multiple Signals**:

It allows combining various signals (e.g., content relevance, user behavior, contextual information) that might not have been considered in the initial ranking.
For example, while the initial retrieval might be based on keyword matching or basic vector similarity, the re-ranking stage can incorporate semantic understanding, user preferences, or engagement metrics.

- **Enhanced User Experience**:

Users are more likely to find the information they need quickly if the results presented to them are more relevant and higher quality.
This can lead to increased satisfaction and engagement with the system.

- **Resource Efficiency**:

Performing complex re-ranking on a smaller subset of documents is more efficient than applying such methods to the entire dataset.

This approach balances computational cost and retrieval quality, ensuring that resources are used effectively.

## Example Use Case
In a typical search engine scenario:

- **1. Initial Retrieval**: A search query is used to retrieve a set of top N documents from the entire corpus using a fast, efficient method (e.g., BM25, TF-IDF).
- **2. Flash Re-ranking**: The top N documents are then re-ranked using a more sophisticated method (e.g., neural re-ranking models, BERT-based models) to better match the user's intent and the semantic meaning of the query.

# Using Google cloud for Lunning Model
Running the Model
The code provided does not run the model on your local machine. Instead, it sends requests to Google's cloud infrastructure where the actual model resides and runs. Here’s why:

- **API Configuration**: By configuring the API key with genai.configure(api_key=GOOGLE_API_KEY), you are setting up authentication for making requests to Google's cloud services.
- **Model Instantiation**: The GenerativeModel instance created is a client-side representation that allows you to send requests to the model hosted in the cloud. It does not download or run the model locally.
## How It Works
- **Request**: When you use this model to generate text or perform other tasks, your code sends a request to Google's cloud servers.
- **Processing**: Google's infrastructure processes the request using the gemini-1.5-pro model.
- **Response**: The results are sent back to your application via the API.
## Example Usage
Here is an example of how you might use this setup to generate text:

```python

import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Instantiate the model
model = genai.GenerativeModel('gemini-1.5-pro')

# Generate text using the model
response = model.generate(prompt="Once upon a time")
print(response['generated_text'])
```
# AutoConfig
## Key Points
- **Loading Configuration**:

```python

config = AutoConfig.from_pretrained(model_name, trust_remote_code=True)
```
- **Modifying Configuration Parameters**:

### Changing the number of labels:
```python

config.num_labels = 5
```
### Adjusting the dropout rate:
```python

config.hidden_dropout_prob = 0.3
```

### Instantiating with Modified Configuration:

```python

tokenizer = AutoTokenizer.from_pretrained(model_name, config=config, trust_remote_code=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, config=config, trust_remote_code=True)
```
## Conclusion
By modifying the configuration parameters, users can adapt pre-trained models to new tasks or specific requirements of their experiments. This flexibility allows for efficient customization without the need to train models from scratch.

### Do Visit 
- [Cohere Reference for Reranking](https://docs.cohere.com/reference/rerank)
