from flask import Flask
from flask_redis import Redis

app= Flask(__name__)
app.config['REDIS_HOST'] = 'localhost'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0
redis= Redis(app)

if __name__== '__main__':
    app.run(debug=True)