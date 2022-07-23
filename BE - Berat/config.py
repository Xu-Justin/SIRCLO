from uuid import uuid4
SECRET_KEY = uuid4().hex
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + './database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True