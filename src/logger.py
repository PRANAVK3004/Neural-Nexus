import logging
import os, errno

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

class Logger:
    def __init__(self, file_name: str = "bot.log", folder: str = "logs"):
        mkdir_p(str(folder))
        self.log_path = f'{folder}/{file_name}'

        logging.root.handlers = []
        logging.basicConfig(format='%(levelname)s | %(asctime)s - %(message)s', datefmt='%Y-%m-%d (%a) %H:%M:%S', level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler(self.log_path)])

    
    def __debug(self, message: str):
        """Log a debug message
        """
        logging.debug(message)

    def __info(self, message: str):
        """Log an info message
        """
        logging.info(message)
        print(f'{message}')
    
    def __warning(self, message: str):
        """Log a warning message
        """
        logging.warning(message)

    def __error(self, message: str):
        """Log an error message
        """
        logging.error(message)

    def __critical(self, message: str):
        """Log a critical message
        """
        logging.critical(message)

    def makeLog(self, message: str, level: str):
        """Make a log message

        Args:
            message (str): Message to log
            level (str): Log level

        Raises:
            ValueError: Invalid log level
        """
        match level.upper():
            case "DEBUG":
                self.__debug(message)
            case "INFO":
                self.__info(message)
            case "WARNING":
                self.__warning(message)
            case "ERROR":
                self.__error(message)
            case "CRITICAL":
                self.__critical(message)
            case _:
                raise ValueError("Invalid log level")