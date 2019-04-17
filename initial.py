from flask import Flask, render_template, request, redirect, url_for ,flash, send_file
import os,subprocess
from werkzeug.utils import secure_filename
from os.path import dirname, abspath
import numpy as np

file_path = dirname(dirname(abspath(__file__)))
UPLOAD_FOLDER = './celery_test/Uploads'
OUTPUT_FOLDER = './celery_test/Outputs'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg','pdf'])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
res = np.array([])
@app.route('/') #Decorator 
def hello():
    return render_template('index.html')

@app.route('/upload') #Decorator 
def helloo():
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def choose_file():
    #return render_template('upload.html')
    #if 'form_choose' in request.form:
    if request.method == 'POST':
        # check if the post request has the file part
        x = request.form['options']
        print(x)
        return render_template('upload.html')
    else:
        return render_template('index.html')
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("HIII")
            flash('No file attached!')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("Hi")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            from celery_test.run_tasks import res_out
            res  = np.copy(res_out)
            return redirect(url_for('return_files',filename=filename))
    return render_template('index.html')  

@app.route('/return-files/')
def return_files():
    if not os.listdir(OUTPUT_FOLDER) :
        return "NO Output"
    else:
        while not np.all(res==True):
            continue
        os.unlink(UPLOAD_FOLDER+"/"+os.listdir(UPLOAD_FOLDER)[0])
        return send_file(OUTPUT_FOLDER+ "/" + os.listdir(OUTPUT_FOLDER)[0], as_attachment=True)

# @app.route('/file-downloads/')
# def file_downloads():
#     try:
#         return render_template('downloads.html')
#     except Exception as e:
#         return str(e)


# @app.route('/task', methods=['GET', 'POST'])
# def run_task():
#     subprocess.call('python -m ../test_celery.run_tasks')

if __name__=='__main__':
    app.secret_key='super secret key'
    app.run(debug=True)
