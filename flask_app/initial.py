from flask import Flask, render_template, request, redirect, url_for ,flash
import os,subprocess
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/') #Decorator 
def hello():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file attached!')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File uploaded successfully"
    return render_template('index.html')  

@app.route('/task', methods=['GET', 'POST'])
def run_task():
    subprocess.call('python -m ../test_celery.run_tasks')

if __name__=='__main__':
    app.secret_key='super secret key'
    app.run(debug=True)
