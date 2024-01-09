"""
algorithms.py - WordReplacer Class

This module contains the WordReplacer class, which is responsible for replacing words in a given text based on a
predefined dictionary of replacements.

Classes:
    WordReplacer: A class for replacing words in a text.

Usage Example:
    replacement_dict = {'apple': 'fruit', 'car': 'vehicle'}
    word_replacer = WordReplacer(replacement_dict)
    original_text = "I have an apple, and I drive my car."
    replaced_text = word_replacer.replace_words(original_text)
    print(replaced_text)
    # Output: "I have an fruit, and I drive my vehicle."

"""

class WordReplacer:
    """
    WordReplacer Class

    This class is designed to replace words in a given text based on a replacement dictionary.

    Attributes:
        replacement_dict (dict): A dictionary containing word replacements.

    Methods:
        replace_words(text: str) -> str:
            Replaces words in the provided text according to the replacement dictionary.

    Usage Example:
        replacement_dict = {'apple': 'fruit', 'car': 'vehicle'}
        word_replacer = WordReplacer(replacement_dict)
        original_text = "I have an apple, and I drive my car."
        replaced_text = word_replacer.replace_words(original_text)
        print(replaced_text)
        # Output: "I have an fruit, and I drive my vehicle."

    """

    def __init__(self, replacement_dict):
        """
        Initialize a WordReplacer object.

        Parameters:
            replacement_dict (dict): A dictionary containing word replacements.
        """
        self.replacement_dict = replacement_dict

    def replace_words(self, text):
        """
        Replace words in the provided text according to the replacement dictionary.

        Parameters:
            text (str): The input text where words will be replaced.

        Returns:
            str: The text with replaced words.

        """
        for original, replacement in self.replacement_dict.items():
            text = text.replace(original, replacement)
        return text
