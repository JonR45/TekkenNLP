# topic_dataframe.py
"""Module contains functions that create topics and build them into a dataframe:

    `_heaviest_words_indices(topic, number_of_words)`
    ``topic_dataframe((model, feature_names, number_of_words))

"""

import pandas as pd

def _heaviest_words_indices(topic, number_of_words):
    """Helper function that returns the x number of words that have been given the greatest 
    weight for a given topic. Used as a helper for the `topic_dataframe` function.


    Parameters
    ----------
    topic : numpy array
        A numpy array that contains the weights given to each word within a topic. The array will 
        be the length of the number of features (words) for a given corpus.


    number_of_words : int
        The number of words with the heaviest weight that you want to return. Think of this as
        the top n words that are connected most strongly to a given topic.

    Returns
    --------
    The indices of the x number_of_words with the greatest weight. i.e., the x most important words
    within a topic.
    
    """
    
    return topic.argsort()[:-number_of_words - 1:-1]   # step of -1 reverses the order so we extract the indices in descending order, starting 
                                                                     # with the highest-scoring word




def topic_dataframe(model, feature_names, number_of_words):
    """Creates a dataframe that shows the x number_of_words with the greatest weight for
    each topc i.e., the most important words for each topic. 

    Parameters
    ----------
    model : scikit-learn NMF model
        The scikit-learn Non-Negative Matrix Factorisation model.

    feature_names : list
        The feature names created from the TF-IDF vectoriser.
        tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

    number_of_words : int
        The x number of most heavily weighted words you want to return.


    Returns
    --------
    df : pandas dataframe
        Dataframe with the x most heavily weighted words and the topic.
    
    
    """
    
    topics = {}
    for topic_index, topic in enumerate(model.components_):
        t = (topic_index)
        topics[t] = [feature_names[i] for i in _heaviest_words_indices(topic, number_of_words)]
    
    return pd.DataFrame(topics)

