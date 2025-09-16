"""
pythonAssessment.py
-------------------
A text analysis tool for a news article.

Functions:
    count_specific_word(text: str, word: str) -> int
    identify_most_common_word(text: str) -> str | None
    calculate_average_word_length(text: str) -> float
    count_paragraphs(text: str) -> int
    count_sentences(text: str) -> int
"""

import re
from collections import Counter
import string


def count_specific_word(text: str, word: str) -> int:
    """
    Count the number of occurrences of a specific word in the text.

    Args:
        text (str): The text to search through.
        word (str): The target word to count.

    Returns:
        int: The count of occurrences. 0 if no matches.
    """
    if not text or not word:
        return 0
    # Case-insensitive, match whole words only
    pattern = rf'\b{re.escape(word)}\b'
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def identify_most_common_word(text: str):
    """
    Identify the most common word in the text.

    Args:
        text (str): The text to analyze.

    Returns:
        str | None: The most common word, or None if text is empty.
    """
    if not text.strip():
        return None
    # Extract words ignoring punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    counter = Counter(words)
    most_common, _ = counter.most_common(1)[0]
    return most_common


def calculate_average_word_length(text: str) -> float:
    """
    Calculate the average length of words in the text, ignoring punctuation.

    Args:
        text (str): The text to analyze.

    Returns:
        float: Average word length. 0 if text is empty.
    """
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0.0
    total_length = sum(len(word.strip(string.punctuation)) for word in words)
    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    """
    Count the number of paragraphs in the text.
    Paragraphs are separated by one or more empty lines.

    Args:
        text (str): The text to analyze.

    Returns:
        int: Number of paragraphs. 1 if text is empty (as per spec).
    """
    if not text.strip():
        return 1
    # Split on two or more newlines
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the text.
    Sentences end with ., !, or ?.

    Args:
        text (str): The text to analyze.

    Returns:
        int: Number of sentences. 1 if text is empty (as per spec).
    """
    if not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings after split
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


if __name__ == "__main__":
    # ----- User Prompt -----
    file_path = input("Enter the path to the news article text file: ").strip()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            article_text = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

    search_word = input("Enter the word you want to count: ").strip()

    print("\n--- Text Analysis Results ---")
    print(f"Occurrences of '{search_word}':",
          count_specific_word(article_text, search_word))
    print("Most common word:",
          identify_most_common_word(article_text))
    print("Average word length:",
          round(calculate_average_word_length(article_text), 2))
    print("Number of paragraphs:",
          count_paragraphs(article_text))
    print("Number of sentences:",
          count_sentences(article_text))