import logging

#################################################
#              create logger
#################################################
logger = logging.getLogger('example')
logger.setLevel(logging.INFO)


#################################################
#              create handler
#################################################
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


#################################################
#              create formatter
#################################################
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s:%(message)s', datefmt='%y-%m-%d %I:%M:%S')


#################################################
#           Add formatter to handler
#################################################
ch.setFormatter(formatter)


#################################################
#           Add handler to logger
#################################################
logger.addHandler(ch)


#################################################
#           Print message with logger
#################################################
logger.debug("This is a debug message")
logger.info("This is a information")
logger.warning("This is a warning message")
logger.error("This is a error message")