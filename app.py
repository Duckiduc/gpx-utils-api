from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'uploads/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/script1', methods=['POST'])
def run_script1():
    if 'file' not in request.files:
        return 'No file selected', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected', 400
    
    if not allowed_file(file.filename):
        return 'Invalid file type. Please select a CSV file.', 400
    
    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER + filename)
    
    subprocess.run(['python', 'script1.py', UPLOAD_FOLDER + filename])
    
    return 'Conversion successful', 200

@app.route('/script2', methods=['POST'])
def run_script2():
    if 'file' not in request.files:
        return 'No file selected', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected', 400
    
    if not allowed_file(file.filename):
        return 'Invalid file type. Please select a CSV file.', 400
    
    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER + filename)
    
    subprocess.run(['python', 'script2.py', UPLOAD_FOLDER + filename])
    
    return 'Conversion successful', 200

@app.route('/script3', methods=['POST'])
def run_script3():
    if 'file' not in request.files:
        return 'No file selected', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected', 400
    
    if not allowed_file(file.filename):
        return 'Invalid file type. Please select a CSV file.', 400
    
    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER + filename)
    
    subprocess.run(['python', 'script3.py', UPLOAD_FOLDER + filename])
    
    return 'Conversion successful', 200

if __name__ == '__main__':
    app.run(debug=True)
