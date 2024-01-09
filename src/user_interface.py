# src/user_interface.py
class UserInterface:
    @staticmethod
    def get_input_file():
        return input("Zadejte cestu k vstupnímu souboru: ")

    @staticmethod
    def get_compression_config():
        return input("Zadejte konfiguraci komprese (slova ke zkrácení): ")

    @staticmethod
    def get_word_replacements():
        replacements = {}
        while True:
            word = input("Zadejte slovo, které chcete nahradit, nebo stiskněte Enter pro ukončení: ")
            if not word:
                break
            abbreviation = input(f"Zadejte zkratku pro slovo '{word}': ")
            replacements[word] = abbreviation
        return replacements

    @staticmethod
    def get_output_file():
        return input("Zadejte název výstupního souboru: ")
