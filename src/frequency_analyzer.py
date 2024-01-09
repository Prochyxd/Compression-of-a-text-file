"""
frequency_analyzer.py - FrequencyAnalyzer Class

This module contains the FrequencyAnalyzer class, which is responsible for analyzing the frequency of words in a given text.

Classes:
    FrequencyAnalyzer: A class for analyzing word frequencies in a text.

Usage Example:
    frequency_analyzer = FrequencyAnalyzer()
    sample_text = "This is a sample text. Sample text is used for demonstration."
    word_counts = frequency_analyzer.analyze(sample_text)
    print(word_counts)
    # Output: Counter({'sample': 2, 'text': 2, 'this': 1, 'is': 1, 'a': 1, 'used': 1, 'for': 1, 'demonstration': 1})

"""

from collections import Counter

class FrequencyAnalyzer:
    """
    FrequencyAnalyzer Class

    This class is designed to analyze the frequency of words in a given text.

    Methods:
        analyze(text: str) -> Counter:
            Analyzes the frequency of words in the provided text and returns a Counter object.

    Usage Example:
        frequency_analyzer = FrequencyAnalyzer()
        sample_text = "This is a sample text. Sample text is used for demonstration."
        word_counts = frequency_analyzer.analyze(sample_text)
        print(word_counts)
        # Output: Counter({'sample': 2, 'text': 2, 'this': 1, 'is': 1, 'a': 1, 'used': 1, 'for': 1, 'demonstration': 1})

    """

    @staticmethod
    def analyze(text):
        """
        Analyze the frequency of words in the provided text and return a Counter object.

        Parameters:
            text (str): The input text to analyze.

        Returns:
            Counter: A Counter object with word frequencies.

        """
        words = text.split()
        word_counts = Counter(words)
        return word_counts
