from flask import Flask
from flask_redis import Redis

app= Flask(__name__)
redis= Redis(app)

if __name__== '__main__':
    app.run(debug=True)