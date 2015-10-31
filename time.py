__author__ = 'IgorP'


from datetime import *; from dateutil.relativedelta import *
"""
trenutno = datetime.now()
print trenutno
print trenutno.year
print trenutno.month
print trenutno.day
print trenutno.hour
print trenutno.minute
print trenutno.second
print int(trenutno.year)

"""
class rojdat():
    leto = 0
    mesec = 0
    dan = 0
    ura = 0
    minuta = 0
    sekunda = 0

    def create(self,l,me,d,u,mi,s):
        self.leto=l
        self.mesec=me
        self.dan=d
        self.ura=u
        self.minuta=mi
        self.sekunda=s
        return self
    def __str__(self):
        return "Primer %s-%s-%s %s:%s:%s" % (self.leto,self.mesec, self.dan, self.ura, self.minuta, self.sekunda)

    def __repr__(self):
        return "Primer %s-%s-%s %s:%s:%s" % (self.leto,self.mesec, self.dan, self.ura, self.minuta, self.sekunda)

igor = datetime(1983, 5, 6, 9, 45)
marusa = datetime(1984, 5, 4, 12, 00)
now = datetime.now()
today = date.today()

def razlika(ime):
    now = datetime.now()
    a = relativedelta(now,ime)
    return a

koncno = razlika(igor)
print koncno.years
print koncno.months
print koncno.days

