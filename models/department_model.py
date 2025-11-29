# here i have created table for department

from database import db 
class Department(db.Model):
    __tablename__ = "departments"
    id= db.Column(db.Integer , primary_key= True )
    name = db.Column(db.String(120))
    description = db.Column(db.Text)
    