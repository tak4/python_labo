import logging.config
import yaml

# loggerの設定
with open("log_config.yaml", "r") as log_spec_file:
    logging.config.dictConfig(yaml.load(log_spec_file, Loader=yaml.FullLoader))

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')