import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])

    # Tokenize and remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS and len(word) > 2]

    # Rejoin tokens
    return ' '.join(tokens)
