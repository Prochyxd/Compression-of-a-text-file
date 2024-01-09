# Compression-of-a-text-file

This Python program is developed for the compression of text files with a .txt extension. It serves as a versatile tool that takes any text file containing natural language text as input and transforms it into another file with a demonstrably reduced size.

## Functionality

### Frequency Analysis
The program incorporates a `FrequencyAnalyzer` class, which conducts a frequency analysis of the words in the input text. This analysis provides insights into the distribution of words and their occurrence frequencies.

### Word Replacement
A key feature is the `WordReplacer` class, responsible for replacing specific words in the input text with user-defined abbreviations. This allows users to customize and compress the text while ensuring readability and preserving the essential content.

### Logging
To maintain transparency and track the program's operations, a `LogManager` class is implemented. It logs various activities, including errors, replacements made, and their details, with a timestamp. Users can choose to print the log and filter entries based on time and other parameters.

### User Interface
The `UserInterface` class facilitates user interaction by providing a guide on how to use the program. It prompts users to input the path to the source text file, guides them through word replacements, and allows them to specify the output file name. Additionally, the interface handles errors gracefully, providing informative messages.

### Main Program
The `main.py` file serves as the entry point to the program. It orchestrates the interaction between the user interface, word replacement algorithms, frequency analysis, and log management. Users are guided through the process, and the compressed text is saved to an output file.

## Requirements

The program adheres to a set of requirements, including configurability, logging, error handling, and modular organization. It is designed to be extensible, with separate modules for the user interface, algorithms, and log management.

While the program currently meets some of the outlined requirements, future enhancements include the addition of unit tests for various functions and the potential generation of auxiliary files, such as coding tables or lists of abbreviations.

The code is organized into distinct directories, including /log for logs, /config for configurations, /data for data and files, and /src for source code modules. External source code is designated to /lib or /vendor, promoting a clean and organized project structure.


# Requirements from my school
- [x] The program takes a single text file as input.
- [x] The output consists of one or more files.
- [x] (This point is addressed by allowing users to adjust the text as they see fit) The text must remain readable by a human and its meaning preserved even after modifications, removals, and replacements of words. In other words, the text can change, such as by removing unnecessary words and irrelevant sentences, but it must not affect the essential content of the text.
- [x] The program must be configurable, specifying which file to process, where to save the result, and how to name it.
- [x] For each text modification, the program must create a log entry containing information about its configuration, the processed content, and whether and how well the compression or decompression was successful, or if an error occurred.
- [x] The program must be capable of displaying information about its operations from the log and allow filtering based on user-defined time and other parameters.
- [x] The program must provide users with help on how to use it.
- [x] The program must not use any external library for compression or decompression.
- [x] The program must handle errors, such as file reading permissions or non-text files. Each error must be logged, and a suitable error message must be displayed to the user.
- [ ] The program must include unit tests demonstrating various functions.
- [x] The program must be divided into multiple files and folders for individual parts. Logs should be in the /log directory, configurations in the /config directory, data and files in the /data directory, source code divided into additional packages/modules in the /src directory (user interface separately, compression algorithms separately, log handling separately). Documentation in the /doc directory and unit tests in the /test directory. If external source code is used, it must be in a separate directory, such as /lib or /vendor.
- [ ] Besides the compressed file, the program may generate auxiliary files, such as a coding table, a list of abbreviations, etc.

# THE DOCUMENTATION FOR MY CODE AND THIS README.MD WAS GENERATED USING AI
