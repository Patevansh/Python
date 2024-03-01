from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    subject=db.Column(db.String(100))

    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")