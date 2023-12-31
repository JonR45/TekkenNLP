# text_cleaning.py
"""Module contains functions that clean strings of text:

    `normalize_text(text)`
    `process_contractions(text)`
    `remove_all_punctuation(text)`
    `remove_emojis(text)`
    `remove_html(text)`
    `remove_html_unescape(text)`

    

"""

import emoji
from bs4 import BeautifulSoup 
import html
import contractions
import re


def normalize_text(text):
    """Lower cases the input text.

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text all in lower case.

    """
    return text.lower()


def process_contractions(text):
    """Expands contractions within the inut text e.g., turns "isn't" into "is not".

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text all in lower case.

    """
    return contractions.fix(text)


def remove_all_punctuation(text):
    """Removes punctuation (including special characters such as "$%^&*" etc.)

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text without punctuation and special characters.

    """
    pattern = r"[^\w\s]"
    return re.sub(pattern, "", text)


def remove_emojis(text):
    """Removes emojis from the input text.

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text without emojis.

    """
    return emoji.replace_emoji(text, "")


def remove_html(text):
    """Removes html entities from the input text.

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text without html.

    Notes
    ------
    Warning: MarkupResemblesLocatorWarning:
        This function returned a Warning due to some (most) comments not containing any html:
        "Warning: MarkupResemblesLocatorWarning: The input looks more like a filename than markup. You may want to open this file and p
        ass the filehandle into Beautiful Soup."
        So, although the warning was harmless and the function worked, it is preferable to use `html.unescape(text)` to handle the 
        'html entities' such as "&quot;"

    """
    try:
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()

    except MarkupResemblesLocatorWarning:
        return text


def remove_html_unescape(text):
    """Removes html entities from the input text.

    Parameters
    -----------
    text : str
        A string of text.

    Returns
    --------
    text : str
        The string of text without html.

    """
    return html.unescape(text)
