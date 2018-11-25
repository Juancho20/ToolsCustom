import os

class Config(object):
	SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite://C:/Users/Juancho/Desktop/pagodiario/data/registro_diario.db'
	