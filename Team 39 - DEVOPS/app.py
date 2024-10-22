from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/api/ipinfo')
def get_ip_info():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)