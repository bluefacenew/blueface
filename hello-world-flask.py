import pkg_resources
pkg_resources.require("Twisted==8.2.0")
import twisted


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
 
