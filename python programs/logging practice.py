##import logging
##logging.basicConfig(filename="ex.log")
##log=logging.getLogger("anyname")
##def fun(a,b):
##    try:
##        if a<b:
##            log.info("correct")
##    except:
##        log.warning("wrong")
##    else:
##        log.critical("failed")
##    finally:
##        print("it is true")
##fun(50,10)

'''example '''
##import logging
##logging.basicConfig(filename="rose.log",level=logging.INFO,format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##logger=logging.getLogger("priya")
##def fun(a):
##    logger.info("enter validation fun")
##    def fun1(user):
##        logger.info("checking data")
##        data=["priyaa"]
##        if user in data:
##            logger.info("username in data")
##            return "welcome"+user
##        else:
##            logger.debug("username not in data")
##            return "wrong user"
##    return fun1
##@fun
##def login(user):
##    return user
##user=input("enter:")
##logger.info("user input given")
##print(login(user))


'''logging to file'''
##from logging import *
##basicConfig(filename="box.log",level=10)
##warning("this is a warning")
##error("this is a error")
##critical("this is a critical")

'''logging to prompt'''

from logging import *
debug("this is debug")
info("this is debug")
warning("this is warning")
error("this is error")
critical("this is critical")
