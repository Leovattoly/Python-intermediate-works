import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
strs = input("Enter a sentence to be stored in the log file: ")
logging.info(strs)