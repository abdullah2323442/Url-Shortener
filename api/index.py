from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Vercel and Flask!'}
