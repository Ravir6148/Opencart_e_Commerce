# import logging
# import os
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger("automationLogger")
#         logger.setLevel(logging.DEBUG)
#         return logger
import logging
import os
import http.client as http_client
import sys

class LogGen:
    @staticmethod
    def loggen():
        logs_dir = os.path.join(os.path.abspath(os.curdir), 'logs')
        os.makedirs(logs_dir, exist_ok=True)

        log_path = os.path.join(logs_dir, 'automation.log')

        # Create logger
        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        logger.handlers.clear()

        # File handler
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Redirect low-level HTTP logs to the file instead of stdout
        http_client.HTTPConnection.debuglevel = 1
        http_log = logging.getLogger("http.client")
        http_log.setLevel(logging.DEBUG)
        http_log.handlers.clear()
        http_log.propagate = False
        http_log.addHandler(file_handler)

        # Configure urllib3 logging
        urllib_logger = logging.getLogger("urllib3")
        urllib_logger.setLevel(logging.DEBUG)
        urllib_logger.handlers.clear()
        urllib_logger.propagate = False
        urllib_logger.addHandler(file_handler)

        # Selenium internal logging
        selenium_logger = logging.getLogger("selenium")
        selenium_logger.setLevel(logging.DEBUG)
        selenium_logger.handlers.clear()
        selenium_logger.propagate = False
        selenium_logger.addHandler(file_handler)

        # WebDriverManager logging
        wdm_logger = logging.getLogger("WDM")
        wdm_logger.setLevel(logging.DEBUG)
        wdm_logger.handlers.clear()
        wdm_logger.propagate = False
        wdm_logger.addHandler(file_handler)

        return logger

