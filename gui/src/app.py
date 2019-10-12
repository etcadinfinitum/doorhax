from flask import Flask, url_for, request, render_template, redirect
import time

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def landing():
    # This is where we would have the image upload 
    # and invoke the Vision service to transform 
    # the image.
    return 'Hello world!'

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
