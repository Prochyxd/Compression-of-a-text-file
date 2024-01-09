# src/user_interface.py
class UserInterface:
    @staticmethod
    def get_input_file():
        return input("Zadejte název vstupního souboru: ")

    @staticmethod
    def get_compression_config():
        return input("Zadejte konfiguraci komprese (např. slova ke zkrácení): ")

    @staticmethod
    def get_output_file():
        return input("Zadejte název výstupního souboru: ")
