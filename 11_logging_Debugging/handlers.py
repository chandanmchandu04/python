import logging

#configuring the basic logging settings
logging.basicConfig(filename='log.hand',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s', force=True)

#adding a file handler with a custom format
file_handler = logging.FileHandler('log.hand')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-%(message)s')
file_handler.setFormatter(formatter)


logging.getLogger('').addHandler(file_handler)


#logging a test message
logging.info("This is my main log")

logger1 = logging.getLogger('user1')
logger2 = logging.getLogger('user2')
logging.info("this is my first login through user1")
logging.debug("After loggingIn this is my first message through user2")