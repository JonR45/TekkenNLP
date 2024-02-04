# Tekken8: Topic Modelling YouTube comments

# Project Overview
- **Programming language**: Python
- **Problem type**: Unsupervised Natural Language Processing
- **Dataset**: YouTube top level comments obtained from the YouTube API
- **Models**: Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorisation (NMF)
- **Notes**:
    - LDA model used Bag of Words for vectorizing, NMF used TF-IDF.
    - Bigram and trigram models were created for the LDA model.
- **Conclusion**: LDA model produced interpretable topics and evaluation scores (coherence 0.44, perplexity -7.47) that met the key results and objective.

  
## Objective
1. Identify human interpretable topics being discussed in response to the Tekken 8 _'New character reveal'_ YouTube video.

## Key results
1. Topics identified
2. Coherence score of >0.4.
3. Perplexity score of <20


## Models
**LDA**
- The LDA model's aim of identifying the underlying topics within a document matched my use case.
- I wanted to use a model that assumed each document (YouTube comment) was a topic and that documents are made up of words that aid in determining the topic.
- I was most interested in determining topics rather than the relationship between words within each document.


**NMF**
- It was hoped the NMF model would be more powerful due to the dimensionality reduction and placing comparatively less weightage to the words with less coherence.

## Evaluation
- The LDA model yielded a coherence score of 0.44 and a perplexity score of -7.47.
- The LDA model's topics were also interpretable and so this model was chosen over the NMF model.


# Visualisation
![coherence_score](/images/coherence_score_0.464_number_of_topics_30.png)
NMF model: finding the number of topics with the highest coherence score

![comment_1_tfidf_scores](/images/tfidf_viz_comment_1.png)
Visualising the TF-IDF scores for one of the comments.

# Conclusion
- The LDA model met the key objective and key results.
- Next steps would be:
    1. Attempt to improve the models by tweaking model parameters such as the number of topics and text vectorization parameters such as minimum and maximum document frequency .
    2. Attempt topic modelling with other models such as BERTopic.

