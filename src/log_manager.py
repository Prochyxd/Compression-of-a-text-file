# src/log_manager.py
import datetime

class LogManager:
    @staticmethod
    def log_activity(action, details):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action}: {details}\n"
        with open("log/activity_log.txt", "a") as log_file:
            log_file.write(log_entry)
