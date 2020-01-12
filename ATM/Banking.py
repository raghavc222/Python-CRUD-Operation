from UserExceptions import *
class Banking:
    def __init__(self):
        self.bal = 500

    def Deposit(self):
        print('-'*40)
        damt = float(input('Enter the amount to deposit :'))    #exception may occur
        print('-'*40)
        if(damt <= 0):
            raise InvalidDepositError('Please enter the valid positive amount ')
        else:
            self.bal = self.bal + damt
            print('Amount Deposited Successfully. Thank you')
        print('-'*40)

    def WithDraw(self):
        print('-'*40)
        wamt = float(input('Enter the amount to withdraw :'))   #Exception may occur
        print('-'*40)
        if(wamt <= 0):
            raise InvalidWithdrawError('Please enter the valid positive amount ')
        if(wamt > 10000):
            raise LimitExceed('Please select amount 10000m or less')
        if((wamt + 500) > self.bal):
            raise InSuffAmtError('Insufficient Balance ')
        else:
            self.bal = self.bal - wamt
            print('Amount Withdrawn Successfully. Thank You')
            print('Current Balance  : ',self.bal)
        print('-'*40)

    def BalEnq(self):
        print('-'*40)
        print('Balance is : ',self.bal)
        print('-'*40)