from flask import Flask,render_template, request,send_file

app=Flask(__name__)
l=[]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload",methods=["post"])
def upload():
    file=request.files["name"]
    filename=request.form['filename']
    ext =file.filename[-4:]
    filenamea=filename+ext
    l.append(filenamea)
    file.save(f'files/{filenamea}')
    return "success"

@app.route("/download")
def download():
    return render_template("download.html",data=l)

@app.route("/getdata",methods=["post"])
def getdata():
    name=request.form["name"]
    return send_file(f'files/{name}')
