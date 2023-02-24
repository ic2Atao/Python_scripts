import os
import logging
import logging.config
import yaml

##################################################
#     Load config information from cfg file
##################################################

# method 1:use config file
#cfg_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger_cfg.conf')
#logging.config.fileConfig(cfg_file_path)

# method 2:use yaml file
cfg_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger_cfg_with_yaml.yml')
with open(cfg_file_path,"r") as f:
    config = yaml.load(f)
    logging.config.dictConfig(config)


##################################################
#                  Create logger 
##################################################
logger = logging.getLogger('simpleExample')


##################################################
#         Print information with logger
##################################################
logger.debug("This is a debug message")
logger.info("This is a information")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.info("This is a test information")