import logging
from logging import FileHandler
from logging import Formatter
import pytest
import datetime


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO


console_log = logging.getLogger('console')


@pytest.fixture()
def test_logger():
    test_log_file = "test.console_log"

    test_logger = logging.getLogger("test_logger")
    test_logger.setLevel(LOG_LEVEL)
    test_logger_file_handler = FileHandler(test_log_file)
    test_logger_file_handler.setLevel(LOG_LEVEL)
    test_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
    test_logger.addHandler(test_logger_file_handler)












@pytest.fixture()
def aggregate_logger():
    PAYMENTS_LOG_FILE = "/tmp/wasted_meerkats/payments.console_log"
    payments_logger = logging.getLogger("wasted_meerkats.payments")

    payments_logger.setLevel(LOG_LEVEL)
    payments_file_handler = FileHandler(PAYMENTS_LOG_FILE)
    payments_file_handler.setLevel(LOG_LEVEL)
    payments_file_handler.setFormatter(Formatter(LOG_FORMAT))
    payments_logger.addHandler(payments_file_handler)