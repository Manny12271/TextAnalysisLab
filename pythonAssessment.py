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
    """Count the number of occurrences of a specific word (case-insensitive)."""
    if not text or not word:
        return 0
    pattern = rf'\b{re.escape(word)}\b'
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def identify_most_common_word(text: str):
    """Identify the most common word in the text."""
    if not text.strip():
        return None
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    counter = Counter(words)
    most_common, _ = counter.most_common(1)[0]
    return most_common


def calculate_average_word_length(text: str) -> float:
    """Calculate the average length of words in the text, ignoring punctuation."""
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0.0
    total_length = sum(len(word.strip(string.punctuation)) for word in words)
    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    """Count the number of paragraphs (blocks separated by empty lines)."""
    if not text.strip():
        return 1
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """Count the number of sentences (split by ., !, or ?)."""
    if not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


if __name__ == "__main__":
    # ----- While loop to ensure a valid file is provided -----
    while True:
        file_path = input("Enter the path to the news article text file: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                article_text = f.read()
            break  # exit while loop if file read successfully
        except FileNotFoundError:
            print("Error: File not found. Please try again.")

    search_word = input("Enter the word you want to count: ").strip()

    print("\n--- Text Analysis Results ---")

    # ----- For loop to display statistics -----
    stats = [
        ("Occurrences of '{}'".format(search_word), count_specific_word(article_text, search_word)),
        ("Most common word", identify_most_common_word(article_text)),
        ("Average word length", round(calculate_average_word_length(article_text), 2)),
        ("Number of paragraphs", count_paragraphs(article_text)),
        ("Number of sentences", count_sentences(article_text))
    ]

    for label, value in stats:
        # ----- Conditional to handle edge cases -----
        if value == 0 or value is None:
            print(f"{label}: No data found")
        else:
            print(f"{label}: {value}")