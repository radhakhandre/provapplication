import logging


class LogGen:
    @staticmethod
    def loggen():
        #    Logging Messages: Use the logger object to record messages at different levels (INFO, WARNING, ERROR, DEBUG, CRITICAL).

        #logging.basicConfig(filename=".//Logs//automation.log", format='%(asctime)s - %(levelname)s - %(message)s',
        #                    datefmt='%m%dpytest -v -s testCases/test_login.py%Y %I:%M:%S %p')
        logging.basicConfig(filename="C://Users//kradh//PycharmProjects//provapplication//Logs//test.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        #logger.setLevel(logging.DEBUG)
        return logger
