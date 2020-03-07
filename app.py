from flask import Flask, render_template, jsonify, url_for, redirect, request
import redis
from flask_redis import FlaskRedis
from datetime import datetime
from rejson import Client, Path

app= Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chain', methods=['GET'])
def mostrar():
    task= r.get("temperatura")
    return render_template('index.html', data=task)

@app.route('/chain', methods=['POST'])
def create():
    temp= request.form['content']
    time1= datetime.now()
    time2= datetime.now()
    r.set("temperatura",str(temp))
    r.set("tiempo1",str(time1))
    r.set("tiempo2",str(time2))
    return render_template((url_for('mostrar'))

if __name__== '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)