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
        log_file_path = "log/activity_log.txt"
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)
        return log_file_path  # Přidáno pro použití v UserInterface

    @staticmethod
    def print_log():
        try:
            with open("log/activity_log.txt", "r") as log_file:
                log_content = log_file.read()
                print("Log content:")
                print(log_content)
        except FileNotFoundError:
            print("Log file not found.")

class UserInterface:
    @staticmethod
    def get_input_file():
        while True:
            try:
                input_file_path = input("Zadejte cestu k vstupnímu souboru: ")
                
                # Kontrola koncovky souboru
                if not input_file_path.endswith('.txt'):
                    raise ValueError("Chyba: Zadaný soubor není souborem s koncovkou .txt.")
                
                with open(input_file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    if not file_content:
                        raise ValueError("Chyba: Zadaný soubor je prázdný.")
                    return input_file_path
            except FileNotFoundError:
                error_message = "Chyba: Zadaný soubor neexistuje. Zadejte platnou cestu k souboru."
                log_file_path = LogManager.log_activity("Error", error_message)
                print(error_message)
                print(f"Chyba byla zaznamenána do logu: {log_file_path}")
            except ValueError as e:
                error_message = str(e)
                log_file_path = LogManager.log_activity("Error", error_message)
                print(error_message)
                print(f"Chyba byla zaznamenána do logu: {log_file_path}")

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

    # Možnost vypsání logu
    print("-------------------------------------------------------------------------------------------")
    print("Chcete vypsat log?")
    print("1 - ano")
    print("2 - ne")
    print("-------------------------------------------------------------------------------------------")
    log = input("Zadejte číslo: ")
    if log == "1":
        LogManager.print_log()
    elif log == "2":
        print("Log nebyl vypsán.")
    else:
        print("Neplatná volba.")

if __name__ == "__main__":
    main()
