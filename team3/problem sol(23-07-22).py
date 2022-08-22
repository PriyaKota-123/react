'''using functools write a program on partialmethod, url_cache and total_ordering'''


'''partail method'''

##from functools import partial
##def mult(a,b):
##    return a*b
##x=2
##f=partial(mult,x)
##result=f(10)
##print(result)
##x=3
##result=f(10)
##print(result)


##from functools import partial
##def f(a,b,c,x):
##    return 1000*a+100*b+10*c+x
##g=partial(f,3,1,4)
##print(g(5))


'''lru_cache'''
##
##from functools import lru_cache
##@lru_cache(maxsize=100)
##def count_vowels(sentence):
##    sentence=sentence.casefold()
##    return sum(sentence.count(vowel)for vowel in 'aeiou')
##print(count_vowels("welcome"))


'''total_ordering'''


from functools import total_ordering
  
@total_ordering
class num:
      
    def __init__(self, value):
        self.value = value
          
    def __lt__(self, other):
        return self.value < other.value
        
    def __eq__(self, other):
        return self.value != other.value
          
print(num(2) < num(3))
print(num(2) > num(3))
print(num(3) == num(3))
print(num(3) == num(5))
