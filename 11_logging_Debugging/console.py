import logging

#configuring the basic logging settings
logging.basicConfig(filename='log.console',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s', force=True)

console_log = logging.StreamHandler()
console_log.setLevel(logging.DEBUG)
format = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-%(message)s')
console_log.setFormatter(format)

logging.getLogger('').addHandler(console_log)

logging.info("This is my main message")
logger3 = logging.getLogger('user3')
logger4 = logging.getLogger('user4')

logging.info("This is for both user3 and user4") 