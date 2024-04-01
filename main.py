from flask import Flask, render_template, request, send_file
import requests
import io
from PIL import Image

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": ""}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    text = request.form['text']
    image_bytes = query({"inputs": text})
    image = Image.open(io.BytesIO(image_bytes))
    
    # Save the image to a temporary buffer
    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
