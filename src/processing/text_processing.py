# text_processing.py
"""Module contains functions that process strings of text:

    `remove_stop_words(text)`
    `tokenize_comment(text)`
    `lemmatize_comment(text)`
    `remove_tekken_character_names_from_tokens`
    `part_of_speech_tagging(text)`


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



def part_of_speech(text):
    """Uses spaCy to return the simple (universal) Part of Speech tag (noun, adjective, verb etc.) for a given text input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    pos : list
        The simple part of speech for each token of the input text.
    
    """
    doc = nlp(text)
    pos = [token.pos_ for token in doc]
    
    return pos



def part_of_speech_tag(text):
    """Uses spaCy to return the detailed part-of-speech tag Part of Speech tag for a given text input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    pos_tags : list
        The part of speech tags for each token of the input text.
    
    """
    doc = nlp(text)
    pos_tags = [token.tag_ for token in doc]
    
    return pos_tags


def part_of_speech_dependency(text):
    """Uses spaCy to return the syntactic dependency, i.e. the relation between tokens
    for a given text input.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    dep_tags : list
        The dependency tags for each token of the input text.
    
    """
    doc = nlp(text)
    dep_tags = [token.dep_ for token in doc]
    
    return dep_tags


def part_of_speech_alpha(text):
    """Uses spaCy to return a boolean value indicating whether the token is an alphanumeric character.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    alpha : list
        The dependency tags for each token of the input text.
    
    """
    doc = nlp(text)
    alpha = [token.is_alpha for token in doc]
    
    return alpha

def part_of_speech_shape(text):
    """Uses spaCy to return the word shape – capitalization, punctuation, digits.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    shape : list
        The shape of the token e.g., xxxxx for lower case (e.g., apple), Xxxxx for capital followed 
        by 4 lower case characters (e.g., Apple), X.X. for something like U.K.
    
    """
    doc = nlp(text)
    shape = [token.shape_ for token in doc]
    
    return shape


def part_of_speech_is_stop(text):
    """Uses spaCy to return a boolean value indicating if the token is a 'stop word'.

    NOTE: "nlp = spacy.load("en_core_web_sm")" needs to be defined outside of the function.

    Parameters
    ----------
    text : str
        A string of text.

    Returns
    -------
    stop_word : list
        A true or false value dependent on whether the word is or is not a stop word.
    
    """
    doc = nlp(text)
    stop_word = [token.is_stop for token in doc]
    
    return stop_word
    

def remove_tekken_character_names_from_tokens(tokens: list):
    """Removes Tekken character names from the comments.

    Parameters
    ----------
    df : pandas dataframe

    Returns
    -------
    df : pandas dataframe
        The input dataframe
    
    """
    tokens_without_character_names = []
    
    tekken_character_names = ['alex', 'alisa', 'bosconovich', 'angel', 'anna', 'williams', 'armor', 'king', 'asuka', 'kazama', 'ayane', 
                              'azazel', 'azucena', 'ortiz', 'baek', 'doo', 'san', 'bruce', 'irvin', 'bryan', 'fury', 'christie', 
                              'monteiro', 'claudio', 'serafino', 'combot', 'cyclops', 'debug', 'devil', 'jin', 'doctor', 
                              'bosconovitch', 'dragunov,', 'sergei', 'eddy', 'gordo', 'eddy', 'gordo', 'eliza', 'fahkumram', 'feng', 'wei', 'forest', 
                              'law', 'ganryu', 'geese', 'howard', 'gigas', 'gon', 'heihachi', 'mishima', 'hwoarang', 'jack', 'jack-7', 
                              'jack-8', 'jin', 'kazama', 'jinpachi', 'mishima', 'josie', 'rizal', 'julia', 'chang', 'jun', 'kazama', 
                              'katarina', 'alves', 'kazumi', 'mishima', 'king', 'kuma', 'kunimitsu', 'lee', 'chaolan', 'leo','kliesen', 
                              'leroy', 'smith', 'lidia', 'sobieska', 'lili', 'de', 'rochefort', 'ling', 'xiaoyu', 'lucky', 'chloe', 
                              'marshall', 'law', 'master', 'raven', 'michelle', 'chang', 'miguel', 'rojo', 'mokujin', 'nancy-mi847j', 
                              'negan', 'nina', 'williams', 'noctis', 'ogre', 'panda', 'paul', 'phoenix', 'rachel', 'reina', 'roger', 'jr', 
                              'sake', 'steve', 'fox', 'tekken', 'force', 'soldier', 'true', 'ogre', 'victor', 'chevalier', 'violet', 
                              'wang', 'jinrei', 'yoshimitsu', 'zafina']

    
    filtered_tokens = [word for word in tokens if word not in tekken_character_names]
    
    tokens_without_character_names.extend(filtered_tokens)

    return filtered_tokens

    