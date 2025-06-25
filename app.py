from flask import Flask, request, render_template, send_from_directory
import os
import json
from extractor import extract_text
from metadata_generator import generate_metadata

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    metadata = None
    file = None  # initialize file variable for template
    if request.method == "POST":
        file = request.files['document']
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            text = extract_text(file_path)
            metadata = generate_metadata(text, file.filename)

            # Save metadata to JSON
            json_path = os.path.join(UPLOAD_FOLDER, file.filename + "_metadata.json")
            with open(json_path, "w") as f:
                json.dump(metadata, f, indent=4)
    
    return render_template("index.html", metadata=metadata, file=file)

# Route to download the JSON
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
