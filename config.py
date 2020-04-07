import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'HARD to guess string'
	MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.163.com')
	MAIL_PORT = int(os.environ.get('MAIL_PORT','25'))
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','true').lower() in ['true','on','1']
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flask Admin <2377388994@qq.com>'
	FLASKY_ADMIN = os.environ.get('Flask_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass

class DevelompentConfig(Config):
	"""生产模式"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://root:@localhost:3306/login'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://' 

config = {
	'development':DevelompentConfig,
	'testing':TestingConfig,

	'default':DevelompentConfig
}
