# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/fetch-product', methods=['POST'])
def fetch_product():
    url = request.json['url']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1').text.strip() if soup.find('h1') else 'Title not found'
        price = soup.find(class_='price').text.strip() if soup.find(class_='price') else 'Price not found'
        description = soup.find(class_='description').text.strip() if soup.find(class_='description') else 'Description not found'
        
        return jsonify({
            'title': title,
            'price': price,
            'description': description
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
