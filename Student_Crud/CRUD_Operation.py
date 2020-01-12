# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:50:57 2020

@author: Raghav

            ***logic for CRUD Operations***
"""
from Menu import Menu 
import sqlite3

conn = sqlite3.connect('stud.db')
print('Conneted Successfully!')

class Operation:
    def select(self):
        sid = int(input('Enter Student Id : '))
        cur = conn.execute('select * from student where sid = %d'%sid)
        res = cur.fetchall()
        if res:
            for rec in res:
                print('Student ID\tStudent Name\tAge\tClass\tLast Percentage\tAddress\tMobile')
                print('{0}\t\t{1}\t\t{2}\t{3}\t{4}\t\t{5}\t{6}'.format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]))    
        else:
            print('No Student exist!!!')

    def insert(self):
        sid = int(input('Enter Student Id : '))
        sname = input('Enter Student Name : ')
        age = int(input('Enter Student Age : '))
        clas = int(input('Enter the Student class : '))
        lp = float(input('Enter last Year Percentage : '))
        adds = input('Enter Student Address : ')
        mob = int(input('Enter Student Number : '))
        selQry = 'Select * from Student where sid = ? and sname = ?'
        cur = conn.execute(selQry,[(sid),(sname)])
        res = cur.fetchall()
        if res:
            for rec in res:
                print('Student Already Exists!!!')
                
        else:
                conn.execute('Insert Into Student values(?,?,?,?,?,?,?)',(sid,sname,age,clas,lp,adds,mob))
                conn.commit()
                print('Student Details Inserted Successfully!!!')
                      
    def update(self):
        while(True):
            try:
                sid = int(input('Enter the id of student :'))
                while(True):
                    print('-'*50)
                    Menu.UpdateMenu()
                    #while(True):
                    ch = int(input('Enter your choice to update : '))
                    if(ch == 1):
                        sname = input('Enter Student Name : ')
                        conn.execute('Update Student Set Sname = "%s" where sid = %d'%(sname,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                    
                    elif(ch == 2):
                        age = int(input('Enter Student Age : '))
                        conn.execute('Update Student Set Age = %d where sid = %d'%(age,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                        
                    elif(ch == 3):
                        clas = int(input('Enter the Student class : '))
                        conn.execute('Update Student Set class = %d where sid = %d'%(clas,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                        
                    elif(ch == 4):
                        lp = float(input('Enter last Year Percentage : '))
                        conn.execute('Update Student Set Last_Perc = %f where sid = %d'%(lp,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                        
                    elif(ch == 5):
                        add = input('Enter Student Address : ')
                        conn.execute('Update Student Set Adds = "%s" where sid = %d'%(add,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                        
                    elif(ch == 6):
                        mob = int(input('Enter Student Number : '))
                        conn.execute('Update Student Set Mob = %s where sid = %d'%(mob,sid))
                        conn.commit()
                        print('Updated Successfully!!!')
                        
                    elif(ch == 7):
                            return False
                    else:
                        print('Invalid Choice!!!')
                        Menu.UpdateMenu()
            except ValueError:
                     print('Please choose from above options!!!')
   
    def delete(self):
        sid = int(input('Enter Student Id : '))
        DelQry = 'delete from student where sid = %d'%sid
        conn.execute(DelQry)
        conn.commit()
        print('Deleted Successfully!!!')
        

        
    
