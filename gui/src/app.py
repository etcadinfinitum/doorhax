from flask import Flask, url_for, request, render_template, redirect, flash
import time
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# We can add more extensions later if we support gifs & video
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index.html')
def landing(filename = None):
    # This is where we would have the image upload 
    # and invoke the Vision service to transform 
    # the image.
    return render_template('main.html', filename=filename)
    # return 'Hello world!'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'user_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        usr_file = request.files['user_file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if usr_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if usr_file and allowed_file(usr_file.filename):
            print('uploading file')
            
            usr_file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(usr_file.filename)))
            # TODO: send the image content as an API call to Google Cloud Platform
            return render_template('main.html',
                                    img=usr_file.filename)
    return redirect(url_for('landing', None))

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
