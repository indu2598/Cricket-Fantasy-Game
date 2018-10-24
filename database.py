import sqlite3
import random
conn = sqlite3.connect("C:\sqlite\Players.db")
c = conn.cursor()


def createTable(teamname):
    c.execute("create table " +teamname +" ('Team','Player','Value')")
def insertTable(teamname):
     c.execute("insert into " +name+ "('Team','Player','Value') values ( 'Team1', 'kholli',120)")  
def selectBTM(tablename):
    c.execute("select Team from team12 WHERE Value = 120")
    for i in c.fetchall():
        print(i)
    
def selectWK(tablename):
    c.execute("select player from " +tablename+ "Where Category = 'WK'")

def selectBWL(tablename):
    c.execute("select player from " +tablename+ "Where Category = 'BWL'")

def selectAR(tablename):
    c.execute("select player from " +tablename+ "Where Category = 'AR'")




name = input("Enter name:")
createTable(name)
insertTable(name)
selectBTM(name)

'''c.execute("create table " +name +" ('Team','Player','Value')")
c.execute("insert into " +name+ "('Team','Player','Value') values ( 'Team1', 'kholli',120)")
c.execute("select * from "+name)
data = c.fetchall()
print(*data)'''


       
