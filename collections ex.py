'''1.orderedict'''

##from collections import *
##r=OrderedDict([(1,"alex"),(2,"john")])
##for k,v in r.items():
##    print(k,v)
##
##print(r)



'''2.default dict'''
##from collections import *
##marks=[("a",1),("b",2),("c",3),("a",5),("c",4)]
##d=defaultdict(list)
##for k,v in marks:
##    d[k].append(v)
##print(list(d.items()))
##

'''3.counter'''

##from collections import *
##d=[('a',1),('b',2),('a',1)]
##c=Counter(name for name,marks in d)
##print(c)


'''4.named tuple'''

##from collections import *
##t=namedtuple("user","name age gender")
##a=t(name="alex",age=25,gender="M")
##print(t)
##print(a.name)
##print(a.age)
##print(a.gender)

'''5.deque'''

##import collections
##name=collections.deque('vicky')
##print('Deque   :',name)
##name.extendleft('....')
##name.append('-')
##print('deque :',name)
