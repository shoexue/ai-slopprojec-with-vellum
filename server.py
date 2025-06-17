from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
from werkzeug.utils import secure_filename
from vellum.client import Vellum
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow requests from your React app

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize Vellum client
vellum_client = Vellum(api_key=os.getenv('VELLUM_API_KEY'))

@app.route('/upload-document', methods=['POST'])
def upload_document():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save the file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Upload to Vellum
        with open(filepath, 'rb') as f:
            result = vellum_client.documents.upload(
                contents=f,
                label=filename,
                add_to_index_names=["myindex"],
                external_id=f"{filename}_{datetime.now().timestamp()}",
                keywords=[],
            )

        # Clean up the temporary file
        os.remove(filepath)

        return jsonify({
            'message': f'Document {filename} uploaded successfully to Vellum',
            'success': True
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Get the user's message from the request
        data = request.get_json()
        user_message = data.get('message', '') if data else ''

        # Run the sandbox module with the user message
        result = subprocess.run(
            ['python3', '-m', 'askmynotes.sandbox', user_message],
            capture_output=True,
            text=True
        )
        
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
