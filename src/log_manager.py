"""
log_manager.py - LogManager Class

This module contains the LogManager class, which is responsible for logging program activities and printing the log content.

Classes:
    LogManager: A class for logging program activities and printing the log content.

Usage Example:
    log_manager = LogManager()
    log_manager.log_activity("Word Replacement", "Replaced words: {'sample': 'smp', 'text': 'txt'}")
    log_manager.print_log()
    # Output: Log content:
    # 2023-01-01 12:00:00 - Word Replacement: Replaced words: {'sample': 'smp', 'text': 'txt'}

"""

import datetime

class LogManager:
    """
    LogManager Class

    This class is designed to log program activities and print the log content.

    Methods:
        log_activity(action: str, details: str) -> str:
            Logs the provided action and details, and returns the path to the log file.
        print_log() -> None:
            Prints the content of the log file.

    Usage Example:
        log_manager = LogManager()
        log_manager.log_activity("Word Replacement", "Replaced words: {'sample': 'smp', 'text': 'txt'}")
        log_manager.print_log()
        # Output: Log content:
        # 2023-01-01 12:00:00 - Word Replacement: Replaced words: {'sample': 'smp', 'text': 'txt'}

    """

    @staticmethod
    def log_activity(action, details):
        """
        Log the provided action and details and return the path to the log file.

        Parameters:
            action (str): The action to be logged.
            details (str): Details or additional information about the action.

        Returns:
            str: The path to the log file.

        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action}: {details}\n"
        log_file_path = "log/activity_log.txt"
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)
        return log_file_path

    @staticmethod
    def print_log():
        """
        Print the content of the log file.

        Raises:
            FileNotFoundError: If the log file is not found.

        """
        try:
            with open("log/activity_log.txt", "r") as log_file:
                log_content = log_file.read()
                print("Log content:")
                print(log_content)
        except FileNotFoundError:
            print("Log file not found.")
