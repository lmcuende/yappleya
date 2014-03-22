import os
import cgi

import webapp2
from google.appengine.ext.webapp import template

AVAILABLE_LOCALES = ['es']

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/index'+'.html'), {}))
class AboutPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/'+'about'+'.html'), {}))
class Book01Page(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/'+'book01'+'.html'), {}))
class Book02Page(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__),'templates/'+'book02'+'.html'), {}))
class PrincipalPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/'+'principal'+'.html'), {}))
class SobrePage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/'+'sobre'+'.html'), {}))
class Libro01Page(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__), 'templates/'+'libro01'+'.html'), {}))
class Libro02Page(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render(os.path.join(os.path.dirname(__file__),'templates/'+'libro02'+'.html'), {}))
app = webapp2.WSGIApplication([('/', MainPage),
							   ('/about', AboutPage),
							   ('/book01', Book01Page),
							   ('/book02', Book02Page),
							   ('/principal', PrincipalPage),
							   ('/sobre', SobrePage),
							   ('/libro01', Libro01Page),
							   ('/libro02', Libro02Page)],
							  debug=True)
