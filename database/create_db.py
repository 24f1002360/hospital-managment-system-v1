
import sqlite3 

# sqlite connection
db = sqlite3.connect('hms.db')
cur = db.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

#Patient 
cur.execute(
    """ CREATE TABLE IF NOT EXISTS patients 
    (id INTEGER PRIMARY KEY AUTOINCREMENT ,
      name TEXT,
      email TEXT ,
      phone TEXT ,
      age INTEGER, 
      gender TEXT,
      password TEXT ,
      status TEXT ) """
)


# doctor 
cur.execute(
    "CREATE TABLE IF NOT EXISTS doctor (id INTEGER PRIMARY KEY AUTOINCREMENT, "
    " name TEXT, specialization_id INTEGER , email TEXT, phone TEXT ,  password TEXT,"
    " status TEXT , availability_notes TEXT)"
)

# Department
cur.execute( "CREATE TABLE IF NOT EXISTS departments ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " 
    "name TEXT, "
    "description TEXT )")

# appointemnt 
cur.execute("""
CREATE TABLE IF NOT EXISTS appointment(
  id INteger PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER ,
  doctor_id INTEGER,
  date TEXT , time TEXT, 
  status TEXT   
)"""            
)


# treatment table
cur.execute(
    """ CREATE TABLE IF NOT EXISTS treatment
    ( id INTEGER PRIMARY KEY AUTOINCREMENT , 
      appointment_id INTEGER, 
      diagnosis  TEXT, 
      prescription TEXT , 
      notes TEXT)""")

# Doctor Availability for 7 days

cur.execute( """ CREATE TABLE IF NOT EXISTS doctor_availability(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    doctor_id INTEGER,
    date TEXT,
    available INTEGER
    )"""
)

# prelogin for admin , check existing admin
cur.execute("SELECT * FROM admin WHERE username=?", ( "admin",))
row = cur.fetchone()

if row is None :
    cur.execute("INSERT INTO admin(username, password) VALUES(?, ?)", ("admin", "admin@123"))
    print("admin user created ") 
else:
    print("admin is already present")  
    
db.commit()
db.close()                 