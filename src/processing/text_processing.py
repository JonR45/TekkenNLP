# text_processing.py
"""Module contains functions that process strings of text:

    `remove_stop_words(text)`
    `tokenize_comment(text)`
    `lemmatize_comment(text)`


"""

import spacy
nlp = spacy.load("en_core_web_sm")


def remove_stop_words(text):
    """Uses spaCy to remove the stop words for a given text input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    text_stop_words_removed : str
        The input text with the stop words removed.
    
    """
    doc = nlp(text)
    tokens_stop_words_removed = [token.text for token in doc if not token.is_stop]
    text_stop_words_removed = " ".join(tokens_stop_words_removed)
    
    return text_stop_words_removed



def tokenize_comment(text):
    """Uses spaCy to tokenize the string passed as input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    text_tokenized : list
        The input text as a list of tokens.
    
    """
    doc = nlp(text)
    tokenized_text = [token.text for token in doc]
    
    return tokenized_text



def lemmatize_comment(text):
    """Uses spaCy to lemmatize (return the base word) for a given text input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    lemmas : list
        The lemmatized versions (base words) of the input text.
    
    """
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    
    return lemmas




    