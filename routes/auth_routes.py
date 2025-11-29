# Here we will do the authentication like when someone enter the system ,then it will check based on the login detail whether user is admin/patient/doctor 
# admin- created by default , doctor - created by admin , patient - can register itself and then login 
# after login each user see there respective dashboard through thi auth
# login, logout , register 

from flask import Blueprint , render_template, request, redirect , session, url_for
from werkzeug.security import generate_password_hash , check_password_hash # for checking passowrd and maintain security 
from database import db

# import for models 
from models.admin_model import Admin
from models.doctor_model import Doctor
from models.patient_model import Patient 

auth_bp = Blueprint("auth_bp", __name__, url_prefix="")

# it will check if it is already login then it will just redirect to dashboard using the session present 
def redirect_after_login():
    role = session.get("role")
    if role == "admin":
        return redirect("/admin/dashboard")
    if role == "doctor":
        return redirect("/doctor/dashboard")
    if role == "patient":
        return redirect("/patient/dashboard")
    return None

# login 
@auth_bp.route("/login", methods=["GET" , "POST"])
def login():
    already = redirect_after_login() # if alaready then use this function
    if already:
        return already
    
    message = None
    if request.method == "POST":
        user_input = request.form.get("email")
        pwd= request.form.get("password")
        
        # admin login check
        admin= Admin.query.filter_by(username=user_input).first()
        if admin and admin.password == pwd:
            session["user_id"]= admin.id
            session["role"]="admin"
            return redirect("/admin/dashboard")
        
        # doctor login check 
        doctor= Doctor.query.filter_by(email=user_input).first()
        if doctor and doctor.password == pwd:
            session["user_id"]=doctor.id
            session["role"]="doctor"
            return redirect("/doctor/dashboard")
        
        # patient login check
        patient = Patient.query.filter_by(email=user_input).first()
        if patient and patient.password == pwd:
            session["user_id"]= patient.id
            session["role"]= "patient"
            return redirect("/patient/dashboard")
        
        message = "Invalid login details. Please try again."
    return render_template("auth/login.html", msg=message )    

# Registration
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    message = None
    if request.method == "POST":
        pname = request.form.get("name")
        pemail= request.form.get("email" )
        pphone= request.form.get("phone")
        page  = request.form.get("age")
        pgen  = request.form.get("gender")
        ppass = request.form.get("password")
        
        # it will check if email already taken or exist
        exist = Patient.query.filter_by(email=pemail).first()
        if exist:
            message = 'Email already registered. Try logging in.'
        else:
            new_p = Patient(
                name=pname , email=pemail , phone=pphone , age=page , gender=pgen, password = ppass , status = "active"
            ) # this new info will now store in patient table later use for login when they try login
            
            db.session.add(new_p) # add the session for the new register     
            db.session.commit()
            
            return redirect("/login")
    return render_template("auth/register.html" , msg=message)

# Logout
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")     