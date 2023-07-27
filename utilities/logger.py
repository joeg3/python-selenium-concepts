import logging
import inspect

class LoggerUtil:
    def getLogger(self):
        # Usual way to have test name displayed in log entries
        logger = logging.getLogger(__name__) # Passing in __name__ makes current file name being executed available for the log entry

        # Since we are doing this by having tests inherit logging class, the logging class is the name displayed in the log entries
        # This hack gets the name of the test
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        file_handler = logging.FileHandler('./logs/logfile.log')

        # <time> : <logger level> : <file name> : <message from log statement> | <filename>:<line number>
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s | (%(filename)s:%(lineno)s)")
        file_handler.setFormatter(format)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO) # Only log INFO and higher, this won't log DEBUG statements
        return logger