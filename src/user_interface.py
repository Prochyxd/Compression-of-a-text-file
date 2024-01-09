"""
user_interface.py - UserInterface Class

This module contains the UserInterface class, responsible for providing a user-friendly interface to interact with the program.

Classes:
    UserInterface: A class for handling user interactions and providing a step-by-step guide.

Usage Example:
    user_interface = UserInterface()
    user_interface.show_guide()
    input_file_path = user_interface.get_input_file()
    word_replacements = user_interface.get_word_replacements()
    output_file_path = user_interface.get_output_file()

"""

from log_manager import LogManager

class UserInterface:
    """
    UserInterface Class

    This class provides a user-friendly interface to interact with the program. It includes methods for showing a guide,
    getting the input file path, obtaining word replacements, and getting the output file path.

    Methods:
        show_guide() -> None:
            Displays a step-by-step guide on how to use the program.
        get_input_file() -> str:
            Prompts the user to enter the path to the input file and performs necessary validations.
            Returns the validated input file path.
        get_word_replacements() -> dict:
            Allows the user to enter words for replacement along with their abbreviations.
            Returns a dictionary of word replacements.
        get_output_file() -> str:
            Prompts the user to enter the name of the output file and performs necessary validations.
            Returns the validated output file path.

    Usage Example:
        user_interface = UserInterface()
        user_interface.show_guide()
        input_file_path = user_interface.get_input_file()
        word_replacements = user_interface.get_word_replacements()
        output_file_path = user_interface.get_output_file()

    """

    @staticmethod
    def show_guide():
        """
        Displays a step-by-step guide on how to use the program.

        """
        print("\nGuide:")
        print("1) Enter the path to the input file. The input file must be a non-empty text file with the .txt extension.")
        print("2) All the words in the input file and their frequencies in the text will be displayed.")
        print("3) Enter a word from the text file that you want to replace, press Enter.")
        print("4) Enter an abbreviation/shortcut for the word you entered before.")
        print("5) Repeat the previous two steps for other words.")
        print("6) Press Enter without entering a word to finish.")
        print("7) Enter the name of the output file with the .txt extension (e.g., example.txt). The output file will be created in the project directory.")
        print("8) The output file contains compressed text.")
        print("9) Choose whether to print the log or not.")

    @staticmethod
    def get_input_file():
        """
        Prompts the user to enter the path to the input file and performs necessary validations.
        Returns the validated input file path.

        Returns:
            str: The path to the validated input file.

        Raises:
            FileNotFoundError: If the specified input file does not exist.
            ValueError: If the specified file is not a .txt file or is empty.

        """
        while True:
            try:
                input_file_path = input("Enter the path to the input file: ")

                # Check the file extension
                if not input_file_path.endswith('.txt'):
                    raise ValueError("Error: The specified file is not a .txt file.")

                with open(input_file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    if not file_content:
                        raise ValueError("Error: The specified file is empty.")
                    return input_file_path
            except FileNotFoundError:
                error_message = "Error: The specified file does not exist. Enter a valid file path."
                log_file_path = LogManager.log_activity("Error", error_message)
                print(error_message)
                print(f"Error has been logged: {log_file_path}")
            except ValueError as e:
                error_message = str(e)
                log_file_path = LogManager.log_activity("Error", error_message)
                print(error_message)
                print(f"Error has been logged: {log_file_path}")

    @staticmethod
    def get_word_replacements():
        """
        Allows the user to enter words for replacement along with their abbreviations.
        Returns a dictionary of word replacements.

        Returns:
            dict: A dictionary containing word replacements and their abbreviations.

        """
        replacements = {}
        while True:
            word = input("Enter the word you want to replace, or press Enter to finish: ")
            if not word:
                break
            abbreviation = input(f"Enter an abbreviation for the word '{word}': ")
            replacements[word] = abbreviation
        return replacements

    @staticmethod
    def get_output_file():
        """
        Prompts the user to enter the name of the output file and performs necessary validations.
        Returns the validated output file path.

        Returns:
            str: The path to the validated output file.

        Raises:
            ValueError: If the specified output file is not a .txt file.

        """
        while True:
            output_file_path = input("Enter the name of the output file with the .txt extension: ")
            if output_file_path:
                if not output_file_path.endswith('.txt'):
                    error_message = "Error: The specified output file is not a .txt file."
                    log_file_path = LogManager.log_activity("Error", error_message)
                    print(error_message)
                    print(f"Error has been logged: {log_file_path}")
                else:
                    return output_file_path
            else:
                print("You entered an empty file name. Enter again.")
