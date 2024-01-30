# Tekken8 Topic Modeling YouTube comments

# Project Overview
- **Programming language**: Python
- **Problem type**: Unsupervised Natural Language Processing
- **Dataset**: YouTube top level comments obtained from the YouTube API
- **Models**: Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorisation (NMF)
- **Notes**: tidbits
- **Conclusion**:

  
## Objective
Identify the topics being discussed in response to the _'New character reveal'_ YouTube video.

## Key results:
- Human interpretable topics
- Coherence score of >0.4.
- Perplexity score of <20


## Models
### LDA
- The LDA model's aim of identifying the underlying topics within a document matched my use case.
- I wanted to use a model that assumed each document (YouTube comment) was a topic and that documents are made up of words that aid in determining the topic.
- I was most interested in determining topics rather than the relationship between words within each document.

### NMF
- I hoped the NMF model would be more powerful due to its dimensionality reduction and placing comparatively less weightage to the words with less coherence.
- NMF is said to act like a filter that can uncover the underlying patterns that really matter - and I hoped this would prove true in this use case.

## Evaluation
### Coherence
LDA: 
NMF:

### Perplexity
LDA:
NMF:

### Human interpretabiliity of the topics
LDA: 

NMF:


# Visualisation
Coherence score visual
HTML visuals

# Next steps


# Installation and Running the Project



You want an average technically competent stranger to be able to read your README file and then run the project on their own. This ensures that more technical hiring managers can reproduce your work and check your code. You can find good README examples
here and here.  https://github.com/VikParuchuri/apartment-finder/blob/master/README.md
https://github.com/dataquestio/loan-prediction/blob/master/README.md


Ideally, you’d also want:
•	Some bullet points with interesting observations you found in exploration
•	Any interesting charts or diagrams you created
•	Information about the model, such as algorithm
•	Error rates and other information about the predictions
•	Any notes about real-world usage of the model
The summary here is that the README is the best way to sell your project, and you shouldn’t neglected. Don’t spend a lot of effort making a good project, then have people skip looking through it because they don’t find it interesting!


It’s important to go through the installation steps yourself in a new folder or on a new computer, to make sure everything works.
