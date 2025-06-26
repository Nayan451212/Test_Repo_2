import logging

class log_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger(__name__)
        log_fail = logging.FileHandler(r"D:\CT_21_batch\Automation_Testing\Project_folder\CredKart_Pytest_Framework_Project\Log\CredKart_file.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s :%(lineno)d :%(message)s")
        log_fail.setFormatter(log_format)
        logger.addHandler(log_fail)
        logger.setLevel(logging.INFO)
        return logger

