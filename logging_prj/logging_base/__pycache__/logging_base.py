import logging
import mylib

#print("#######################################################")
#print("#              This is a simple example                ")
#print("#######################################################")
#logging.info("This is a information")
#logging.warning("This is a warning")
#print(2*('\n'))


#print("#######################################################")
#print("#              Output log to file                      ")
#print("#######################################################")
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
#logging.debug('This is debug level to logfile')
#logging.info('This is info level to log file')
#logging.warning('This is warning level to log file')
#logging.error('This is error level to log file')


#print("#######################################################")
#print("#              Using logging in multi files            ")
#print("#######################################################")
def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s' ,level=logging.DEBUG, datefmt='%y-%m-%d %I:%M:%S')
    #2.logging.basicConfig(format='%(levelname)s:%(message)s' ,level=logging.DEBUG)
    #1.logging.basicConfig(filename='multi_file_example.log', encoding='utf-8', level=logging.INFO)
    logging.info("I want to do something")
    mylib.do_something()
    logging.info("I have done")

def Using_var():
    logging.info("%s before you %s", 'look', 'leap!')

if __name__ == '__main__':
    main()
    Using_var()