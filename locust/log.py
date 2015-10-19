import logging


def setup_logging(loglevel, logfile):
    pass

console_logger = logging

# configure python-requests log level
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)
