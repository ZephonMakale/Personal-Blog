import os

class Config:
    
    SECRET_KEY = 'pitch'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macbookpro:1Chelsea@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_API_KEY = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
    SENDER_EMAIL ='zephon.makalle@gmail.com'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macbookpro:1Chelsea@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://macbookpro:1Chelsea@localhost/blog"
    DEVELOPMENT = True
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
