import datetime

import cgi
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2

## Stores the time the database was last updated

class updateTime(ndb.Model):
        last_updated = ndb.DateTimeProperty(auto_now_add=True)
