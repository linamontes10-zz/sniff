import webapp2
from google.appengine.ext import ndb

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        first_student = Student(first_name='Cesar', last_name='Pablo', credits=11)
        Cesars_input = Wand(core='phoenix', special='feather', wood='chestnut', length=9000)
        Cesars_input.put()
        first_student.put()
        self.response.write(first_student)
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
class Student(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    credits = ndb.IntegerProperty()
    def __str__(self):
        return "%s %s has %s credits." % (self.first_name, self.last_name, self.credits)
class Wand(ndb.Model):
    core = ndb.StringProperty()
    special = ndb.StringProperty()
    wood = ndb.StringProperty()
    length = ndb.FloatProperty()
