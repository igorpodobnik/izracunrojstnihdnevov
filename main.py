#!/usr/bin/env python
import os
import jinja2
import webapp2
from datetime import *
from dateutil.relativedelta import *
from obletnica import *
from seznam_main import build1
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

igor = datetime(1983, 5, 6, 9, 45)
now = datetime.now()
jani = datetime(1947,8,25,6,00)
janidat = date(1947,8,25)
# html fonti http://www.w3schools.com/cssref/css_websafe_fonts.asp
# dateutil link https://labix.org/python-dateutil
class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        para = relativedelta(now,igor)
        para2 = relativedelta(now,jani)
        jed = izracun()
        dorojdneva = izracunrojdneva(janidat)
        params = {"sporocilo": "Tukaj sem tudi jaz, MainHandler",
                  "let": para.years,
                  "mesec": para.months,
                  "dni":para.days,
                  "ur": para.hours,
                  "minut": para.minutes,
                  "obletnica":jed,
                  "let_jani": para2.years,
                  "mesec_jani": para2.months,
                  "dni_jani":para2.days,
                  "ur_jani": para2.hours,
                  "minut_jani": para2.minutes,
                  "dorojdneva" : dorojdneva
                  }

        self.render_template("hello.html", params=params)

class seznamHandler(BaseHandler):
    def get(self):
        params = build1()
        print params
        print "zgoraj"
        self.render_template("timelist.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/seznam', seznamHandler),
], debug=True)
