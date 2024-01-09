# main.py
import os
import sys
from frequency_analysis import FrequencyAnalyzer
from user_interface import UserInterface
from word_replacer import WordReplacer
from log_manager import LogManager

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

    print("Frekvence slov:")
    print(word_counts)

    # ...

    # Získání konfigurace od uživatele
    config = UserInterface.get_compression_config()

    # Získání nahrazovaných slov a jejich zkratek
    replacements = UserInterface.get_word_replacements()

    # Nahrazení slov podle konfigurace
    word_replacer = WordReplacer(replacements)
    compressed_text = word_replacer.replace_words(input_text)

# ...

    # Záznam do logu
    action_details = f"Compression configuration: {config}, Replaced words: {replacement_dict}"
    LogManager.log_activity("Compression", action_details)

    # Uložení komprimovaného textu do výstupního souboru
    output_file_path = UserInterface.get_output_file()
    with open(output_file_path, "w") as file:
        file.write(compressed_text)

if __name__ == "__main__":
    main()
