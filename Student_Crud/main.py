# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:20:08 2020

@author: Raghav

            !!!Main Program!!!
"""

from CRUD_Operation import Operation
from RegLog import RegisLog
from Menu import Menu
import sys

reg = RegisLog()
op = Operation()
while(True):
    try:
        while(True):
            print('-'*50)
            Menu.RegMenu()
            ch = int(input('Enter Your Choice : '))
            if(ch == 1):
                try:
                    reg.register()
                except ValueError:
                    print('Please Enter Valid Input(Number)!!! ')
            elif(ch == 2):
                for i in range(0,3):
                    try:
                        loginStatus = reg.login()
                        while(loginStatus == True):
                            print('-'*50)
                            Menu.StudMenu()
                            ch = int(input('Enter Your choice : '))
                            if(ch == 1):
                                try:
                                    op.select()
                                except ValueError:
                                    print('Please Enter Valid Input(Number)!!! ')
                            if(ch == 2):
                                try:
                                    op.insert()
                                except ValueError:
                                    print('Please Enter Valid Input(Number)!!! ')
                            if(ch == 3):
                                try:
                                    op.update()
                                except ValueError:
                                    print('Please Enter Valid Input(Number)!!! ')
                            if(ch == 4):
                                try:
                                    op.delete()
                                except ValueError:
                                    print('Please Enter Valid Input(Number)!!! ')
                            if(ch == 5):
                                loginStatus = False        
                    except ValueError:
                        print('Please choose from above options!!!')
            elif(ch == 3):
                sys.exit()
            else:
                print('Please Enter Valid Input(Number)!!! ')
    except ValueError:
        print('Please choose from above options!!!')
