import os
from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = '/uploads'  

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        confirmation_message = "File uploaded successfully."

        return render_template('index.html', confirmation_message=confirmation_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
