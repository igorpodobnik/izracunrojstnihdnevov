fg__author__ = 'Igor'
#from dateutil.relativedelta import *
from datetime import *
from obletnica import izracunrojdneva
import operator



igor = date(1983,5,6)
marusa = date(1984,5,4)


lista = [igor,marusa]
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
    for i in lista:
        #print i
        print "zagnal se je build"
        item(i)
    #sorted(diction.items(), key=lambda x: x[1])
    #diction.update({"_kljuc":lista})
    return diction

#ime od spremeljivke.
def ime_sprem(variable):
 for name in globals():
     if eval(name) == variable:
        return name

build1()

print diction
#print varname(igor)




