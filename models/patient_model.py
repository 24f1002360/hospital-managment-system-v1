# here i have creted patient table 
from database import db 

class Patient(db.Model):
    __tablename__ = "patients"
    id= db.Column(db.Integer, primary_key= True )
    name= db.Column(db.String(120))
    email= db.Column(db.String(120) , unique= True)
    phone= db.Column(db.String(20))
    age= db.Column( db.Integer)
    gender = db.Column(db.String(20) )
    password= db.Column(db.String(120))
    status = db.Column(db.String(20))
    
    