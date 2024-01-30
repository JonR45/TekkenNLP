# Tekken8 Topic Modeling YouTube comments

# Project Overview
- **Programming language**: Python
- **Problem type**: Unsupervised Natural Language Processing
- **Dataset**: YouTube top level comments obtained from the YouTube API
- **Models**: Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorisation (NMF)
- **Notes**: tidbits
- **Conclusion**:

  
## Objective
Identify human interpretable topics being discussed in response to the _'New character reveal'_ YouTube video.

## Key results:
- Topics identified
- Coherence score of >0.4.
- Perplexity score of <20


## Models
**LDA**
- The LDA model's aim of identifying the underlying topics within a document matched my use case.
- I wanted to use a model that assumed each document (YouTube comment) was a topic and that documents are made up of words that aid in determining the topic.
- I was most interested in determining topics rather than the relationship between words within each document.


**NMF**
- I hoped the NMF model would be more powerful due to its dimensionality reduction and placing comparatively less weightage to the words with less coherence.
- NMF is said to act like a filter that can uncover the underlying patterns that really matter - and I hoped this would prove true in this use case.

## Evaluation
**Coherence**


LDA: 
NMF:

**Perplexity**


LDA:
NMF:



# Visualisation
Coherence score visual
HTML visuals

# Conclusion
- 

