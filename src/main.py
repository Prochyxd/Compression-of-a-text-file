# main.py
from frequency_analysis import FrequencyAnalyzer
from user_interface import UserInterface
from word_replacer import WordReplacer
from log_manager import LogManager

def main():
    # Získání vstupního textu
    input_file = UserInterface.get_input_file()
    with open(input_file, "r") as file:
        input_text = file.read()

    # Frekvenční analýza slov
    frequency_analyzer = FrequencyAnalyzer()
    word_counts = frequency_analyzer.analyze(input_text)

    # Získání konfigurace od uživatele
    config = UserInterface.get_compression_config()

    # Nahrazení slov podle konfigurace
    replacement_dict = dict(item for item in word_counts.items() if item[1] > 1)
    word_replacer = WordReplacer(replacement_dict)
    compressed_text = word_replacer.replace_words(input_text)

    # Záznam do logu
    action_details = f"Compression configuration: {config}, Replaced words: {replacement_dict}"
    LogManager.log_activity("Compression", action_details)

    # Uložení komprimovaného textu do výstupního souboru
    output_file = UserInterface.get_output_file()
    with open(output_file, "w") as file:
        file.write(compressed_text)

if __name__ == "__main__":
    main()
