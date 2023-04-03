
#1.logging to file

'''from logging import *
basicConfig(filename="logfile303.log")
warning("This is Warning")
error("This is Error")
critical("This is Critical")

output:

WARNING:root:This is Warning
ERROR:root:This is Error
CRITICAL:root:This is Critical
WARNING:root:This is Warning
ERROR:root:This is Error
CRITICAL:root:This is Critical'''

#2.LOGGING TO PROMPT

'''from logging import*
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

output:
WARNING:root:this is warning
ERROR:root:this is error
CRITICAL:root:this is critical'''


#3.CHANGELEVEL

from logging import *
basicConfig(filename="logfile300.log",level=20)
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("tis is critical")

##output:
##
##DEBUG:root:this is debug
##INFO:root:this is info
##WARNING:root:this is warning
##ERROR:root:this is error
##CRITICAL:root:tis is critical

#4.CHANGEFILEMODE

'''from logging import *
basicConfig(filename="log200.log",level=DEBUG,filemode="w")
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

output:

DEBUG:root:this is debug
INFO:root:this is info
WARNING:root:this is warning
ERROR:root:this is error
CRITICAL:root:this is critical'''


#5.FORMAT LOG DATA

'''from logging import *
basicConfig(filename="logfile400.log",level=DEBUG,filemode='w',format='%(asctime)s -- %(message)s')
debug("this is debug")
info("this is error")
warning("this is warning")
error("this is error")
critical("this is critical")


output:

2022-08-11 10:29:10,391 -- this is debug
2022-08-11 10:29:10,391 -- this is error
2022-08-11 10:29:10,391 -- this is warning
2022-08-11 10:29:10,391 -- this is error
2022-08-11 10:29:10,391 -- this is critical'''


#6.FORMAT LOG DATA 2

'''from logging import *
LOG_FORMAT = '%(asctime)s // %(message)s // %(lineno)d'
basicConfig(filename="log500.log",level=WARNING,filemode='w',format=LOG_FORMAT)
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

output:

2022-08-11 10:35:24,003 // this is warning // 97
2022-08-11 10:35:24,003 // this is error // 98
2022-08-11 10:35:24,003 // this is critical // 99'''

#7.CHANGE FORMAT STYLE

'''from logging import *
LOG_FORMAT = "{lineno} ***{name}***{asctime} *** {message}"
basicConfig(filename="log600.log",level=DEBUG,filemode= "w", style='{',format=LOG_FORMAT)
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

output:

112 ***root***2022-08-11 10:46:03,898 *** this is debug
113 ***root***2022-08-11 10:46:03,898 *** this is info
114 ***root***2022-08-11 10:46:03,898 *** this is warning
115 ***root***2022-08-11 10:46:03,898 *** this is error
116 ***root***2022-08-11 10:46:03,898 *** this is critical'''


#8.GET LOGGER

'''from logging import *
LOG_FORMAT ='{lineno} *** {name} *** {asctime} ***{message}'
basicConfig(filename="log700.log",level=DEBUG,filemode='w',style='{',format=LOG_FORMAT)
logger=getLogger("priya")
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")

output:
133 *** priya *** 2022-08-11 10:54:30,388 ***this is debug
134 *** priya *** 2022-08-11 10:54:30,388 ***this is info
135 *** priya *** 2022-08-11 10:54:30,388 ***this is warning
136 *** priya *** 2022-08-11 10:54:30,388 ***this is error
137 *** priya *** 2022-08-11 10:54:30,388 ***this is critical'''


'''import logging    
logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
logger=logging.getLogger('priya')
def validation(fun):
    logger.info("entered validation function")
    def fun(user_input):
        logger.info("before checking in data")
        data=['priya']
        if user_input in data:
            logger.info("username present in database")
            return 'welcome'+user_input
        else:
            logger.debug("username not present in database")
            return "wrong user"
        return fun
@validation
def login_user(user_input):
    return user_input
user_input=input("enter username")
logger.info("user input given")
print(login_user(user_input))

output:

priya
welcome priya'''
  

##def fun(a,b):
##    if(b==0):
##        return abs(a)
##    else:
##        return fun(b,a%b)
##a=90
##b=80
##print("the gcd of 90 and 80 is:",end=" ")
##print(fun(a,b))
##


for i in a:
    for j in (i,a+1):
        for k in (j,a+1):
            print()
