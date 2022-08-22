##Given a sentence as input print all the unique combinations of two words in lexicographical order
##explanation:
##if given sentence is raju plays cricket the possible combintion of two are (cricket,plays),(cricket,raju),(plays,raju).
##input:
##raju play cricket
##output:
##cricket plays
##cricket raju
##plays raju

'''from itertools import combinations
n=input("enter a string").split()
n.sort()
a=combinations(n,2)
b=list(a)
for i in b:
  print(" ".join(i))

output:
enter a string :raju plays cricket
cricket plays
cricket raju
plays raju'''


 
