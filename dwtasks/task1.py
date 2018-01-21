import pandas as pd


def cnvrt(t):
    t = float(t)
    to_23 = t*(0.23)
    to_50 = t*(0.5)
    to_260 = t*(2.60)
    return to_23,to_50,to_260


def result(x):
    to_23,to_50,to_260 = cnvrt(x)
    return to_23,to_50,to_260,"---------->",x



def modify(data):
    if type(data)==dict:
        for i in data.keys():
            if i=='quantity'and data[i]!=0:
                u=result(data[i])
                print u
            modify(data[i])
    elif type(data)==list:
        for i in data:
            modify(i)

x = pd.read_json('data.json', typ='series')
for i in x.keys():
    modify(x[i])

