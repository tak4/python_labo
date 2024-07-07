import logging
import argparse

parser = argparse.ArgumentParser(description='My program')
parser.add_argument('--log', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='ログレベル')

args = parser.parse_args()
loglevel = args.log

print(loglevel)

print(loglevel.upper())
numeric_level = getattr(logging, loglevel.upper(), None)
print('log level: %s' % loglevel)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=numeric_level)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
