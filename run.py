import re
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS, cross_origin
import json
import sqlite3
import random
import datetime

app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods = ['GET','POST'])
@cross_origin()
def home():
    conn = sqlite3.connect('sensordata.db')
    cur = conn.cursor()
    res = cur.execute("select Humidity,Temperature from weatherdata order by rowid desc limit 1")
    res = list(res)[::-1]
    num1 = random.uniform(-80,100)
    num2 = random.uniform(-80,100)
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")
    cur.execute(f"insert into weatherdata values('{date}','{time}','{num1}','{num2}')")
    conn.commit()
    response = jsonify(res)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__=="__main__":
    app.run(debug=True)
