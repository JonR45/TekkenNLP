# text_processing.py
"""Module contains functions that process strings of text:

    `remove_stop_words(text)`
    `tokenize_comment(text)`
    `lemmatize_comment(text)`
    `part_of_speech(text)`
    `part_of_speech_tag(text)`
    `part_of_speech_dependency(text)`
    `part_of_speech_alpha(text)`
    `part_of_speech_shape(text)`
    `part_of_speech_is_stop(text)`
    `remove_tekken_character_names_from_tokens(tokens)`
    `remove_tiny_tokens(tokens)`
    `unique_words_from_tokens(tokens)`
    `word_count(text)`

    # Not used
    `tokenize_string(text)` # this achieves the same result as toeknize_comment()


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
    
    tekken_character_names = ['akuma', 'alex', 'alisa', 'alves', 'angel', 'anna', 'armor', 'asuka', 'ayane', 'azazel', 'azucena', 'baek', 'bob', 'bobb', 'bosconovich', 
                              'bosconovitch', 'bruce', 'bryan', 'chang', 'chang', 'chaolan', 'chevalier', 'chloe', 'christie', 'claudio', 'combot', 'craig',
                              'cyclops', 'de', 'debug', 'devil', 'doctor', 'doo', 'dragunov', 'eddie', 'eddy', 'eddy', 'eddychristie', 'eliza', 'fahkumram',
                              'feng', 'force', 'forest', 'fox', 'fury', 'ganryu', 'geese', 'gigas', 'gon', 'gordo', 'gordo', 'heihachi', 'howard', 'hwoarang',
                              'irvin', 'jack', 'jack-7', 'jack-8', 'jin', 'jin', 'jinpachi', 'jinrei', 'josie', 'jr', 'julia', 'jun', 'katarina',
                              'kazama', 'kazama', 'kazama', 'kazumi', 'kazuya', 'kazuya', 'king', 'king', 'kliesen', 'kuma', 'kunimitsu', 'law', 'lee',
                              'lei', 'leo', 'leroy', 'lidia', 'lili', 'ling', 'lucky', 'lydia', 'marduk', 'marsxhall', 'master', 'michelle', 'miguel',
                              'mishima','mishima', 'mishima', 'mokujin', 'monteiro', 'nancy-mi847j', 'negan', 'nina', 'nina williams', 'ninawilliams',
                              'noctis', 'ogre', 'ogre', 'ortiz', 'pachi', 'panda', 'paul', 'phoenix', 'rachel', 'raven', 'reina', 'richard', 'rizal',
                              'rochefort', 'roger', 'rojo', 'sake', 'san', 'serafino', 'sergei', 'saheen', 'shaheen', 'smith', 'sobieska', 'soldier', 'steve', 'tekken', 'true',
                              'trueogre', 'victor', 'violet', 'wang', 'wei', 'williams', 'wulong', 'xiaoyu', 'yoshi', 'yoshimitsu', 'yoshimitsus', 'zafina']

    
    filtered_tokens = [word for word in tokens if word not in tekken_character_names]
    
    tokens_without_character_names.extend(filtered_tokens)

    return filtered_tokens


def remove_tiny_tokens(tokens):
    """Removes tokens with less than 3 characters e.g., "fd", "a" etc.

    Parameters
    ----------
    tokens : list
        The list of tokens.

    Returns
    -------
    tokens : list
        The input list without tokens containing <=2 characters.
    
    """
    return [token for token in tokens if len(token) >2]




def unique_words_from_tokens(tokens): 
    """Function that removes duplicate words from a list of tokens.

    Parameters
    -----------
    tokens : list
        List of tokens.

    Returns
    -------
    unique_words_list : list
        List of unique words in the input list.
    
    
    """
    unique_words_list = []
    [unique_words_list.append(x) for x in tokens if x not in unique_words_list]
    return unique_words_list



def word_count(text):
    """Splits a string of a text by a space, turns it into a list and returns
    the length of the list to provide the number of words in the input string.

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    -------
    word_count : integer
        The number of words in the input string.
    """
    number_of_words = len(str(text).split(' '))

    return number_of_words


def tokenize_string(text):
    """Uses a regex pattern to extract sequences of two or more word characters (letters, digits, and underscores) as 
    tokens. Whitespace characters (spaces, tabs, newlines) act as natural boundaries between tokens. 
    
    
    Used as part of topic modeling project and will be used to take a string of topics and create a list.

    Parameters
    -----------


    Returns
    --------
    A list of strings, where each string represents a single word extracted from the input text.


    Notes
    ------
    r"\w\w+":
        The pattern seeks two consecutive word characters, encountering a non-word character (including whitespace) prevents further 
        matching, effectively treating it as a word boundary.

    Example
    --------
    Input: 
        tokenize_topic("cat dog tree chocolate.")
    
    Output: 
        ['cat', 'dog', 'tree', 'chocolate']
    
    """
    
    return re.findall(r"\w\w+", text)

    