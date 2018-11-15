from __future__ import unicode_literals
import logging
#from threading import localhost
from django.db import connections
from lg.models import UserProfile
#relationships across databases are not allowed

''' this class is the router for the authentication DB
'''
#class AuthRouter(object):
    #def db_for_read(self, model, **hints):
        #if model._meta.app_label == 'auth':
            #return 'auth_db'
        #return None

    #def db_for_write(self, model, **hints):
        #if model._meta.app_label == 'auth':
            #return 'auth_db'
        #return None

    #def allow_relation(self, obj1, obj2, **hints):
        #if obj1._meta.app_label == 'auth' or \
            #obj2._meta.app_label == 'auth':
            #return True
        #return None

    #def allow_migrate(self, db, app_label, model_name=None, **hints):
        #if app_label == 'auth':
        #return None

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        #this method is passed as a model
        return random.choice(['slave1', 'slave2', 'slave3', 'slave4'])


    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'slave1', 'slave2', 'slave3', 'slave4')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, lg, model_name=None, **hints):
        return True
