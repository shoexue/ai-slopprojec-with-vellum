from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Allow requests from your React app

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Get the user's message from the request
        data = request.get_json()
        user_message = data.get('message', '') if data else ''

        # Check if a file was uploaded
        if 'file' in request.files:
            file = request.files['file']
            if file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Run the sandbox module with the file path and user message
                result = subprocess.run(
                    ['python3', '-m', 'askmynotes.sandbox', user_message, filepath],
                    capture_output=True,
                    text=True
                )
                
                # Clean up the uploaded file
                os.remove(filepath)
                
                return jsonify({
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                    'returncode': result.returncode
                })
        
        # If no file was uploaded, just run the sandbox module with the user message
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
