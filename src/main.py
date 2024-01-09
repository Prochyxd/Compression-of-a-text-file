# main.py
import os
import sys
from collections import Counter
import datetime

class FrequencyAnalyzer:
    @staticmethod
    def analyze(text):
        words = text.split()
        word_counts = Counter(words)
        return word_counts

class LogManager:
    @staticmethod
    def log_activity(action, details):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action}: {details}\n"
        with open("log/activity_log.txt", "a") as log_file:
            log_file.write(log_entry)

class UserInterface:
    @staticmethod
    def get_input_file():
        return input("Zadejte cestu k vstupnímu souboru: ")

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
        while True:
            output_file_path = input("Zadejte název výstupního souboru (nechte prázdné pro výchozí): ")
            if output_file_path:
                return output_file_path
            else:
                print("Zadali jste prázdný název souboru. Zadejte znovu.")

class WordReplacer:
    def __init__(self, replacement_dict):
        self.replacement_dict = replacement_dict

    def replace_words(self, text):
        for original, replacement in self.replacement_dict.items():
            text = text.replace(original, replacement)
        return text

def main():
    # Zajisti, že projekt_root je v sys.path
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(project_root)

    # Získání vstupního textu
    input_file_path = UserInterface.get_input_file()
    with open(input_file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    # Výpis slov z vstupního textu
    print("Slova ve vstupním textu:")
    print(input_text.split())

    # Frekvenční analýza slov
    frequency_analyzer = FrequencyAnalyzer()
    word_counts = frequency_analyzer.analyze(input_text)

    print("-------------------------------------------------------------------------------------------")
    print("Frekvence slov:")
    print(word_counts)

    # Získání nahrazovaných slov a jejich zkratek
    replacements = UserInterface.get_word_replacements()

    # Nahrazení slov podle konfigurace
    word_replacer = WordReplacer(replacements)
    compressed_text = word_replacer.replace_words(input_text)

    # Záznam do logu
    action_details = f"Replaced words: {replacements}"
    LogManager.log_activity("Word Replacement", action_details)

    # Uložení komprimovaného textu do výstupního souboru
    output_file_path = UserInterface.get_output_file()
    with open(output_file_path, "w") as file:
        file.write(compressed_text)

if __name__ == "__main__":
    main()
