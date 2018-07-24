import webapp2
import jinja2
import os
from google.appengine.ext import ndb

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('/templates/homepage.html')
        self.response.write(template.render())
    def post(self):
        new = self.request.get('posts')
        template = jinja_current_dir.get_template('')

class PlaydateHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('/templates/playdate.html')
        self.response.write(template.render())
    def post(self):
        zipcode = self.request.get('zipcode')
        template_vars = {
            'zipcode' : zipcode,
        }

        template = jinja_current_dir.get_template('/templates/newplaydate.html')
        self.response.write(template.render(template_vars))

class DogParksHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('/templates/dogparks.html')
        self.response.write(template.render())
    def post(self):
        new = self.request.get('posts')
        template = jinja_current_dir.get_template('')

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('/templates/aboutus.html')
        self.response.write(template.render())
    def post(self):
        new = self.request.get('posts')
        template = jinja_current_dir.get_template('')


app = webapp2.WSGIApplication([
    ('/home', HomeHandler),
    ('/dogparks', DogParksHandler),
    ('/playdate', PlaydateHandler),
    ('/aboutus', AboutUsHandler),
], debug=True)
