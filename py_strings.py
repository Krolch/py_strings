"""
mandatory docstring module
"""
import string
def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    txet=text[::-1]
    return txet



def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    Text=''
    first_letter=True
    for c in text:
        if c in string.whitespace or c in string.punctuation:
            Text += c
            first_letter=True
            continue
        if c in string.digits:
            Text += c
            first_letter=False
            continue
        if c.islower() and first_letter:
            Text += c.upper()
            first_letter=False
            continue
        Text += c
        first_letter=False
    return Text



def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    a = ["a","e","i","o","u","y","ą","ę","ó"]
    return sum(map(text.lower().count, a))



def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    return sum(int(x) for x in text if x.isdigit())



def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
#    text=text.lower()
#    text.find(sub)==-1
#    text.find(sub.upper())==-1
#    text.find(sub)!=-1
#    text=text.lower()
#    sub=sub.lower()
#
#    numbuh=0
#    if sub in text:
#        numbuh=numbuh
#    else:
#        numbuh=numbuh+1
#    return numbuh

#s.find(a)
    n=text.find(sub)
    if n == -1:
        a = None
    else:
        a = n
    return a
