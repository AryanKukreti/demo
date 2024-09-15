from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Ensure this folder exists or create it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

# Route for the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the home page (home.html)
@app.route('/home')
def home():
    return render_template('home.html')

# Route for the contact page (contact.html)
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle file uploads
@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect(url_for('index'))

    return 'Failed to upload file', 400

# Route to handle contact form submissions
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Print contact information to the console for this example
    print(f"Contact form submitted:\nName: {name}\nEmail: {email}\nMessage: {message}")

    return 'Thank you, we have received your message.', 200

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
