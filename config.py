# In this file i will do the config part like secret key , SQLite file path and SQLAlchemy settings 
import os 
Dir = os.path.abspath( os.path.dirname(__file__) )
class Config:
    SECRET_KEY = "kanchan@choiminho"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(Dir , "hms.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 