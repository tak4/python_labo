import logging
from logging import config
import yaml

with open("./log_setting/log_spec.yaml", "r") as log_spec_file:
    config.dictConfig(yaml.load(log_spec_file, Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
logger.debug('This message should go to the log file')
