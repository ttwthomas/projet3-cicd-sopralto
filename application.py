from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!!!!'

application.add_url_rule('/', 'index', (hello_world))


@application.route('/health')
def health():
    return { "app": "ok","db_connection": "ok","version": "1.0.0"}

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')
