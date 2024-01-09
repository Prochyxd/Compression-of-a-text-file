"""
main.py - Main Program

This module contains the main program that orchestrates the compression of a text file.

Modules:
    os: Provides a way of using operating system-dependent functionality.
    sys: Provides access to some variables used or maintained by the interpreter and functions that interact strongly with the interpreter.
    UserInterface: Module handling user interactions and providing a step-by-step guide.
    WordReplacer: Module containing the WordReplacer class for word replacement operations.
    FrequencyAnalyzer: Module containing the FrequencyAnalyzer class for word frequency analysis.
    LogManager: Module containing the LogManager class for logging program activities.

Functions:
    main() -> None:
        The main function that coordinates the execution of the program. It guides the user, analyzes word frequencies,
        performs word replacement, logs activities, and saves the compressed text to an output file.

Usage Example:
    if __name__ == "__main__":
        main()

"""

import os
import sys
from user_interface import UserInterface
from algorithms import WordReplacer
from frequency_analyzer import FrequencyAnalyzer
from log_manager import LogManager

def main():
    """
    The main function that orchestrates the compression of a text file.

    This function guides the user through the compression process, analyzes word frequencies, performs word replacement
    based on user input, logs activities, and saves the compressed text to an output file.

    """
    read_guide = input("Do you want to read the guide? (yes/no): ")
    if read_guide.lower() == "yes":
        UserInterface.show_guide()
        input("Press Enter to continue.")
    
    # Ensure that project_root is in sys.path
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(project_root)

    # Get input text
    input_file_path = UserInterface.get_input_file()
    with open(input_file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    # Print words from the input text
    print("Words in the input text:")
    print(input_text.split())

    # Word frequency analysis
    frequency_analyzer = FrequencyAnalyzer()
    word_counts = frequency_analyzer.analyze(input_text)

    print("-------------------------------------------------------------------------------------------")
    print("Word frequencies:")
    print(word_counts)

    # Get replacement words and their abbreviations
    replacements = UserInterface.get_word_replacements()

    # Replace words according to the configuration
    word_replacer = WordReplacer(replacements)
    compressed_text = word_replacer.replace_words(input_text)

    # Log the activity
    action_details = f"Replaced words: {replacements}"
    LogManager.log_activity("Word Replacement", action_details)

    # Save compressed text to the output file
    output_file_path = UserInterface.get_output_file()
    with open(output_file_path, "w") as file:
        file.write(compressed_text)

    # Print the log
    print("-------------------------------------------------------------------------------------------")
    print("Do you want to print the log? (yes/no): ")
    print_log = input()
    if print_log.lower() == "yes":
        LogManager.print_log()

if __name__ == "__main__":
    main()
