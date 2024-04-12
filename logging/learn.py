#logging module wile give us everything to we need to report and record  the progress and problem

#logging allows us to write status messages to a file or other output streams. the message contains information on which parts of your code have executed and what problems may have arrived 
#each log message has a level the five build in levels are
#NOTSET = 0
#debug --10
#info  --20
#warning -30
#error --40
#critical --50
#_--- if user wants they can create there own additional levels ----------
import logging
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\Lenovo\\PYTHON\\Lytx-CFP-DataEngg-AWS\\LOGGING\\logger.Log",level=logging.DEBUG, format =log_format)
logger = logging.getLogger()
# test the logger
logger.info("Our first message.")
print(logger.level)

'''import logging
name = 'GFG'
logging.error('%s raised an error', name)'''

'''#logging module wile give us everything to we need to report and record  the progress and problem

#logging allows us to write status messages to a file or other output streams. the message contains information on which parts of your code have executed and what problems may have arrived 
#each log message has a level the five build in levels are
#NOTSET = 0
#debug --10
#info  --20
#warning -30
#error --40
#critical --50
#_--- if user wants they can create there own additional levels ----------'''