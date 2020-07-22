from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route('/health')
def health():
    return { "app": "ok","db_connection": "ok","version": "1.0.0"}