from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///user.sqlite3'
app.config['SQALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    roll=db.Column(db.String(50))
    subject=db.Column(db.String(50))
    contact=db.Column(db.String(50))
    
    def __init__(self,name,roll,subject,contact):
        self.name=name
        self.roll=roll
        self.contact=contact
        self.subject=subject

with app.app_context():
    db.create_all()

data=[
    {
        "name":"Vansh",
        "roll":"25",
        "subject":"python",
        "contact":"9054255770"
        },
    {
        "name":"Rahul",
        "roll":"14",
        "subject":"Os",
        "contact":"7896541230"
        },
    {
        "name":"Sugam",
        "roll":"23",
        "subject":"Coma",
        "contact":"6542153987"
        }
        ]
@app.route("/upload")
def upload():
    for i in data:
        stud=Student(i["name"],i["roll"],i["subject"],i["contact"])
        db.session.add(stud)
    db.session.commit()
    return "success"

@app.route("/")
def home():
    data=Student.query.all()
    return render_template("home.html",data=data)