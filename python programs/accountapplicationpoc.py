##create a banking application,to check current balance,to deposite,to withdraw.
##
##account class
##atributes-name,balance,min_balance
##methods-deposite,withdraw,printstatement
##
##currentaccount class.....currentaccount balance
##atributes-name,balance
##methods- __str__
##give min_balance
##
##
##saving account class.....currentaccount balance
##atributes-name,balance
##methods- __str__
##
##deposit rs.5000 in saving account
##withdraw rs.7000 from saving
##
##input:
##1.print current balance
##2.print current balance after deposit-5000
##3.print current balance after withdraw-10000
##4.withdraw 6000 rupees
##
##output:
##1.print current balance 10000
##2.print current balance after deposit-15000
##3.print current balance after withdraw-5000
##4.insufficient balance
 
import sys
class Account:
    def __init__(self):
        self.balance=0
        print("account is created")
    def deposite(self):
        amount=int(input("enter the amount to deposite:"))
        self.balance+=amount
        print('ur new balance=%d'%self.balance)
    def withdraw(self):
        amount=int(input('enter amount to withdraw:'))
        if(amount>self.balance):
            print('insufficient balance!')
        else:
            self.balance-=amount
            print('your remaining balance =%d'%self.balance)
    def enquiry(self):
        print('your balance =%d'%self.balance)
a=Account()
a.deposite()
a.withdraw()
a.enquiry()
