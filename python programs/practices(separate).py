##import datetime
##from datetime import date
##import re
##def fun(n):
##    #n=input("enter a number")
##    return re.finditer(r'(\d{4})-(\d{1,2})-(\d{1,2})',n)
##print(fun('2019-09-09'))
##
##
##import datetime
##from datetime import date
##import re
##def fun(n):
##    n=input("enter a number")
##    a=re.finditer(r'(\d{4})-(\d{1,2})-(\d{1,2})',n)
##date=datetime.datetime.strptime(a.group(),'%y-%m-%d').date()
##print(fun(n))

import datetime
from datetime import date
import re
s ="Jason's birthday is on 1991-09-21"
match = re.(r'\d{4}-\d{2}-\d{2}', s)
date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
print(date)
