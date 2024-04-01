from flask import Flask, render_template, request, jsonify
import requests
import io
from PIL import Image

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

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
    image.show()
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
