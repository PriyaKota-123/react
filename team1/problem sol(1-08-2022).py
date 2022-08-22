##Today's task for you guys will be to develop your first-ever Python game i.e., "Snake Water Gun."
##
##Most of you must already be familiar with the game. Still, I will provide you with a brief description.
##
##This is a two-player game where each player chooses one object.  As we know, there are three objects, snake, water, and gun. So, the result will be 
##
##Snake vs. Water: Snake drinks the water hence wins.
##Water vs. Gun: The gun will drown in water, hence a point for water
##Gun vs. Snake: Gun will kill the snake and win.
##In situations where both players choose the same object, the result will be a draw.
##Now moving on to instructions:
##You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
##You do not have to use a print statement in case of the above function.
##Then you have to give input from your side.
##After getting ten consecutive inputs, the computer will show the result based on each iteration.
##You have to use loops(while loop is preferred).

import random
lst = ['snake','water','gun']
rand = random.choice(lst)
print('select 0 for snake, select 1 for water, select 2 for gun')

n = 10
while n>0:
    user = int(input('enter ur option:'))
    
    if user==0 and lst.index(rand)==1:
        print('snake drinks the water hence snake wins')

    elif user==1 and lst.index(rand)==2:
        print('gun will drown in water, hence a point for water')

    elif user==2 and lst.index(rand)==0:
        print('Gun will kill the snake and win')
        
    else: 
        print('draw')

    n-=1
