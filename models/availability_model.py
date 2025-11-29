# this is the availability table for doctor 
from database import db
class DoctorAvailability(db.Model):
    __tablename__ = "doctor_availability"
    id= db.Column(db.Integer , primary_key=True)
    doctor_id = db.Column(db.Integer , db.ForeignKey( "doctor.id"))
    date= db.Column(db.String(50))
    available= db.Column(db.Integer)
    doctor= db.relationship("Doctor")
    
    