fg__author__ = 'Igor'
#from dateutil.relativedelta import *
from datetime import *
from obletnica_temp import izracunrojdneva




igor = date(1983,5,6)
marusa = date(1984,5,4)


list = [igor,marusa]
diction = {}
temp_diction = {}

#definiranje posameznega vnosa v seznam
def item(ime):
    rez = izracunrojdneva(ime)
    diction.update({ime_sprem(ime):rez})
    #print ime_sprem(ime)
    #print rez
    return

#Buildanje seznama

def build1():
    for i in list:
        #print i
        item(i)

#ime od spremeljivke.
def ime_sprem(variable):
 for name in globals():
     if eval(name) == variable:
        return name

build1()

print diction
#print varname(igor)




