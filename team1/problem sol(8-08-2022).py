## Write a  Python Program using Multithreading ,
##Consider a couple who is having a Joint account and both are having their ATM cards.
##They come to different ATMs and try to withdraw some amount at the same time.
##Let’s say the total balance in the account is 500 and Wife tries to withdraw 450
##and the husband tries to withdraw 100. When they swipe the card for withdrawing money,
##the balance shown will be 500. Two threads will be created for the transaction,
##out of which only one thread should be successful and the other should fail.
##If both the threads get successful then its a loss to the bank.
##So, the threads should be in synchronization so that one fails and the other wins.'''

from threading import *

class Atm:
    def __init__(self, amount):
        self.amount = amount
        self.l = Lock()
        print('init method called')
        
    def withdraw(self, withamount):
        name = current_thread().name
        self.l.acquire()
        if withamount > self.amount:
            print('withdrawing amount for {name} is more than current balance')

        else:
            print(f'{withamount} for {name} amount withdraw successful')
            self.amount -= withamount
            print(self.amount)
        self.l.release()

obj = Atm(500)
t1 = Thread(target=obj.withdraw, args=(450,), name='wife')
t2 = Thread(target=obj.withdraw, args=(200,), name='husband')
t1.start()
t2.start()
t1.join()
t2.join()






