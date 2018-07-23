import webapp2
from google.appengine.ext import ndb

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('sniff.html')
        self.response.write(template.render())
    def post(self):
        new = self.request.get('posts')
        template = jinja_current_dir.get_template('')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
