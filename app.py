# import the important libraries
from flask import Flask, Request, render_template, redirect, url_for, request
from ocr_engine import OCREngine
from utils.helper import allowed_filename, save_uploaded_file
import os, sys

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# ensure that uploads folder exists in directory
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.mkdir(app.config['UPLOAD_FOLDER'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_filename(file.filename):
            filename = save_uploaded_file(file)
            if filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                ocr = OCREngine()
                extract_text = ocr.extract_text(file_path=file_path)
                return render_template("index.html", extract_text = extract_text)
            return redirect(url_for('index'))
        return render_template("index.html", extract_text = None)


if __name__ == '__main__':
    app.run(debug=True)