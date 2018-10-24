import sqlite3
conn = sqlite3.connect("C:\sqlite\Cricket.db")
c = conn.cursor()

def batting(scores,faced,hc,c,fours, sixes):
    bpoints = 0
    bpoints = scores/2
    
    #points for half century and century
    bpoints = bpoints+ 5*hc
    bpoints = bpoints+ 10*c

    #points for fours and sixes
    bpoints = bpoints + fours
    bpoints = bpoints+ sixes*2
        
    #points for strike rate
    sRate = (scores/faced)*100
    if sRate >= 80 and sRate<100:
        bpoints = bpoints+ 2
    elif sRate >=100:
        bpoints = bpoints+ 4
    return bpoints
#Points for bowling, twickets means total wickets and n wickets means number of wickets per innings###

def bowling(twicket , bowled, maiden,given):
    tpoints = 0
    #points for each wickets
    tpoints = twicket*10
    
    #points for economy rate
    if bowled == 0 and given ==0:
        tpoints = tpoints+0
    else:
        erate = given/ ((bowled/6)+maiden)
        if erate >= 3.5 and erate <4.5:
            tpoints = tpoints + 4
        elif erate >= 2 and erate <3.5:
            tpoints = tpoints + 7
        elif erate < 2:
            tpoints = tpoints + 10

    #points for wickets per inning
    if twicket == 3:
        tpoints = tpoints+ 5
    elif twicket >= 5:
        tpoints = tpoints +10

    
    return tpoints

#points for fieling
def fielding(catch,stamping,runout):
    fpoints = 0
    field = catch+stamping+runout
    fpoints = fpoints + field*10
    return fpoints

def virtualtable():
    c.execute("CREATE TABLE match AS (SELECT Players, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches,Stamping, RO FROM MainTable);")
        
        
