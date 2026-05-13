import logging #python's built in logging-module, this module provides logging.info()
#logging.warning(), logging.error()


def setup_logger(): # so that we can reuse this function (logger setup) everywhere

    logger = logging.getLogger("network_test_framework") # get a logger with name

    if not logger.handlers: # if logger doesnt exists create one, if already exists, return the same one
# does this already have one?
        logger.setLevel(logging.INFO) #setting logging level

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ) #defines how logs look like

        console_handler = logging.StreamHandler() # creates a console handler
#logs will be printed to terminal
        console_handler.setFormatter(formatter) #attaches the formatter

        logger.addHandler(console_handler) #connects handle to the logger

    return logger