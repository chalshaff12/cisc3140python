import os
basedir = os.path.abspath(os.path.dirname(__file__))

#secret_key for flask-wtf form security
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	