from flask_venv import Flask, request, render_template, jsonify
import pytesseract

from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        text = extract_text_from_image(filepath)
        return jsonify({'text': text})
    return jsonify({'error': 'File not uploaded'})

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = search_notes(query)
    return jsonify({'results': results})

def search_notes(query):
    # Dummy search implementation
    # In a real application, you would search a database or index
    return ["Note 1: Example content", "Note 2: Example content"]

if __name__ == '__main__':
    app.run(debug=True)