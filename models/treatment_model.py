# this the treatment table for patient prescribed by doctor
from database import db 
class Treatment (db.Model) :
    __tablename__ = "treatment"
    id= db.Column(db.Integer, primary_key = True)
    appointment_id= db.Column( db.Integer , db.ForeignKey("appointment.id" ))
    diagnosis = db.Column( db.Text )
    prescription = db.Column(db.Text)
    notes = db.Column(db.Text)
    appointment = db.relationship("Appointment")
    
    
