# here i have created the doctor table 
from database import db
class Doctor(db.Model):
    __tablename__="doctor"
    
    id= db.Column(db.Integer , primary_key= True)
    name= db.Column(db.String(120))
    specialization_id = db.Column(db.Integer, db.ForeignKey("departments.id") )
    email= db.Column(db.String(120) , unique=True)
    phone= db.Column(db.String(20) )
    password = db.Column(db.String(120))
    status = db.Column(db.String(20))
    availability_notes = db.Column(db.Text )
    department= db.relationship("Department")
    
    