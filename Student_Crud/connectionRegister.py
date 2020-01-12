# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:04:16 2020

@author: Raghav
"""
#Imports
import sqlite3

#Creating Connection
conn = sqlite3.connect('stud.db')
print('Conneted Successfully!')

#Creation Of Table
creReg = 'create table Register(Rid INT, Uname TEXT, Email TEXT, Password TEXT, Re_write_Password TEXT)'
conn.execute(creReg)
print('Register Table Created Successfully\n')

creStud = 'create table Student(Sid INT, Sname TEXT, Age INT, Class INT, LastPerc REAL, Adds TEXT, Mob INT)'
conn.execute(creStud)
print('Student Table Created Successfully')


