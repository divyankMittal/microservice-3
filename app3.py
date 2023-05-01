from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import pymongo


   
   
 


app = Flask(__name__)

@app.route("/getdata" , methods=['GET'])
def func():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['divyank']
    collection = db['mySampleCollection']
    if request.method=="GET":
       #name = request.form['fname']
       allDocs = collection.find({}) 
       return render_template("index4.html", var=allDocs)
 


if __name__ == '__main__':
     print("run APP")
     app.run(host='0.0.0.0', port=80)