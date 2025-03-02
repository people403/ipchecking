from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Tambahkan ini

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk semua request

@app.route('/get-ip', methods=['GET'])
def get_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Ambil data lokasi dari ip-api.com
    response = requests.get(f"http://ip-api.com/json/{user_ip}")
    ip_data = response.json()

    return jsonify({
        'ip': user_ip,
        'country': ip_data.get('country'),
        'region': ip_data.get('regionName'),
        'city': ip_data.get('city'),
        'isp': ip_data.get('isp'),
        'latitude': ip_data.get('lat'),
        'longitude': ip_data.get('lon'),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
