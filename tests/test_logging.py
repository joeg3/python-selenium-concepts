from utilities.logger import LoggerUtil

class TestLoggerExample(LoggerUtil):
    
    def test_logging_test_case(self):
        logger = self.getLogger()

        # Order of logging levels
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

