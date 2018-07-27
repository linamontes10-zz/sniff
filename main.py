import webapp2
import jinja2
import urllib
import os
from google.appengine.ext import ndb
from model import *

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
        # Only zip code search
        print(self.request)
        name = self.request.get('name')
        if not name:
            zipcode = self.request.get('zipcode')
        # add dog to zip code
        else:
            ownername = self.request.get('ownername')
            breed = self.request.get('breed')
            age = self.request.get('age')
            size = self.request.get('size')
            personality = self.request.get('personality')
            email = self.request.get('email')
            zipcode = self.request.get('zipcode')
            image = str(self.request.get('image'))

            dog_post = Dog(name=name,ownername=ownername,breed=breed,age=int(age),size=size,personality=personality, email=email,zipcode=int(zipcode), image=image)
            dog_key = dog_post.put()

        zipcode_query = Dog.query(Dog.zipcode==int(zipcode))
        check_zipcode_query = zipcode_query.fetch()

        # if name:
        #     check_zipcode_query.insert(0, dog_post)

        if not check_zipcode_query:
            dogs = Dog.query().fetch()
            dogsfound = False
        else:
            dogs = check_zipcode_query
            dogsfound = True

        template_vars = {
            'dogs' : dogs,
            'dogsfound' : dogsfound,
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

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        dog_key = self.request.get('id')
        dog_key_object = ndb.Key(urlsafe=dog_key)
        dogimage = dog_key_object.get()

        print(dogimage)

        if dogimage.image:
            self.response.headers['Content-Type'] = "image/jpg"
            self.response.out.write(dogimage.image)
        print("Lina is here")

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template('/templates/aboutus.html')
        self.response.write(template.render())
    def post(self):
        new = self.request.get('posts')
        template = jinja_current_dir.get_template('')


app = webapp2.WSGIApplication([
    ('/image', ImageHandler),
    ('/home', HomeHandler),
    ('/', HomeHandler),
    ('/dogparks', DogParksHandler),
    ('/playdate', PlaydateHandler),
    ('/aboutus', AboutUsHandler),
], debug=True)
