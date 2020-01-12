from Menu import Menu
from Banking import Banking
from UserExceptions import *
import sys
bo = Banking()
while(True):
    Menu.menu()
    try:
        ch = int(input('Enter your selection: '))
        if(ch == 1):
            try:
                bo.Deposit()
            except ValueError:
                print('Please enter only Numbers')
            except InvalidDepositError as ide:
                print(ide)
        elif(ch == 2):
            try:    
                bo.WithDraw()
            except ValueError:
                print('Please enter only Numbers')
            except InvalidWithdrawError as iwe:
                print(iwe)
            except LimitExceed as le:
                print(le)
            except InSuffAmtError:
                print('You dont have sufficient Amount')
        elif(ch == 3):
            bo.BalEnq()
        elif(ch == 4):
            sys.exit
        else:
            print('Please enter a Valid Choice!!')
    except ValueError:
        print('Please enter only Numbers')