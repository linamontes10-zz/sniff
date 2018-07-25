from google.appengine.ext import ndb

class Dog(ndb.Model):
    name = ndb.StringProperty()
    ownername = ndb.StringProperty()
    breed = ndb.StringProperty()
    age = ndb.IntegerProperty()
    size = ndb.StringProperty()
    personality = ndb.StringProperty()
    email = ndb.StringProperty()
    zipcode = ndb.IntegerProperty()
