# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:54:40 2020

@author: Raghav

#logic for login and Register
"""

from Menu import Menu
import sqlite3
conn = sqlite3.connect('stud.db')
print('Conneted Successfully!')
cursor = conn.cursor()
    
class RegisLog:
    def register(self):
        Rid = int(input('Enter Rid : '))
        Uname = input('Enter Username :')
        Email = input('Enter Email : ')
        Password = input('Enter Password(only letters) :')
        Re_write_Password = input('Re-Enter Password : ')
        selQry = 'Select * from Register where Rid = ? and Uname = ? and Password = ?'
        cur = conn.execute(selQry,[(Rid),(Uname),(Password)])   #parameter is: List of Tuples [(Rid),(Uname)..]
        res = cur.fetchall()
        if res:
            for i in res:
                print('User Already Exsits!!!')
                return
        else:
            if(Password == Re_write_Password):
                conn.execute('Insert Into Register values(?,?,?,?,?)',(Rid,Uname,Email,Password,Re_write_Password))
                conn.commit()
                print('Registered Successfully!! Please Login To Access')
                return
            else:
                print('Password does not match!!!')
            
              
    def login(self):
        Uname = input('Username : ')
        Password = input('Password : ')
        selQry = 'Select * from Register where Uname =? and Password = ?'
        cur = conn.execute(selQry,[(Uname),(Password)])
        res = cur.fetchall()
        if res:
            for i in res:
                print('-'*50)
                print('Welcome {0}'.format(i[1]))
                print('-'*50)
                return True
        else:
            print('Username or Password is Invalid!!!')
            return False

                
                
            
            
            
            
          
    
