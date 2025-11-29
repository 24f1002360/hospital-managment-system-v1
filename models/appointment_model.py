# this is the appointment table i created 
from database import db 

class Appointment(db.Model):
    __tablename__ = "appointment"
    id= db.Column( db.Integer , primary_key=True)
    patient_id = db.Column(db.Integer , db.ForeignKey("patients.id") )
    doctor_id= db.Column(db.Integer, db.ForeignKey( "doctor.id" ))
    date = db.Column(db.String(50))
    time = db.Column( db.String(50))
    status = db.Column(db.String(20) )
    patient = db.relationship("Patient")
    doctor= db.relationship("Doctor")
    