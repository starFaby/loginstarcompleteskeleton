import os
class Config:
    SECRET_KEY = 'starfaby'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/flaskmysql'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

