__author__ = 'Franko'


from datetime import *; from dateutil.relativedelta import *


def izracun():
    today = date.today()
    obletnica = date(today.year,11,14)
    koliko = obletnica - today

    if koliko.days < 0:
        novoleto = today.year + 1
        obletnica=date(novoleto,11,14)

    koliko = obletnica - today
    return koliko.days

def izracunrojdneva(ime):
    today = date.today()
    obletnica = ime
    obletnica=date(today.year,obletnica.month,obletnica.day)
    koliko = obletnica - today


    if koliko.days < 0:
        novoleto = today.year + 1
        obletnica=date(novoleto,obletnica.month,obletnica.day)
    koliko = obletnica - today
    return koliko.days

