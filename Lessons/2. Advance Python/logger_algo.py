import logging


logger = logging.getLogger(__name__)        #creating logger
logger.setLevel(logging.INFO)               #setting level [LVL PRIORITY (CRITICAL, ERROR, WARNING, INFO, DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')   #setting a format. time name message
handler = logging.FileHandler('Log.log')    #.txt or .log file name or file to be log
handler.setFormatter(formatter)             #adding a format to handler
logger.addHandler(handler)                  #adding handler to logger


if __name__ == "__main__":
    logger.info('PROGRAM EXECUTED')         #log when executed