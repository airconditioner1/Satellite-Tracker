from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apod')
def apod():
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'R7QYL8yzkLmejHQHrM2tp1OtU37qJz7j8M6sntLA'
    response = requests.get(api_url, params={'api_key': api_key})
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch APOD data'})

if __name__ == '__main__':
    app.run(debug=True)
