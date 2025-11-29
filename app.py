# In this file i will load the config of config.py and initialize SQLAlchemy to create default admin and then later i will create all the tables 
from flask import Flask 
from config import Config 
from database import db
from models.admin_model import Admin
from models.patient_model import Patient
from models.department_model import Department
from models.doctor_model import Doctor
from models.appointment_model import Appointment
from models.treatment_model import Treatment 
from models.availability_model import DoctorAvailability 
from routes.auth_routes import auth_bp # calling auth 

 # pre admin
 
def create_default_admin() :
    from models.admin_model import Admin
    admin = Admin.query.filter_by(username="kanchanadmin").first() 
    if not admin:
        new_admin = Admin(username="kanchanadmin" , password= "choiminho")
        db.session.add(new_admin)
        db.session.commit()
        print("ADMIN CREATED")
    else:
        print("ADMIN ALREADY EXIST") 
 
# config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # this will create table and admin
    with app.app_context():
        db.create_all()
        create_default_admin()
     
    app.register_blueprint(auth_bp) 
        
    return app  

       
if __name__ == "__main__" :
    app = create_app()
    app.run(debug=True)    
    
