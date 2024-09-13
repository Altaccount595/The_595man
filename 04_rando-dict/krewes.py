import random
krewes = {3:['Jonthan','Alex','Naf'], 42:['Jonthan','Alex','Naf'], 888:['Jonthan','Alex','Naf']}

def randoselect():
    x=int(random.random()*3)
    lis=list (krewes.keys())
    z=int(random.random()*3)
    print((krewes.get(lis[x]))[z])
randoselect()