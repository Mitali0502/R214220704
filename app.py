import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def fetch_numbers_from_url(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            if 'numbers' in data:
                return set(data['numbers'])  # Using a set to ensure uniqueness
    except requests.exceptions.RequestException:
        pass  # Ignore URLs that take too long to respond or are invalid
    return set()

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd"
    ]
    
    unique_numbers = set()
    
    for url in urls:
        unique_numbers.update(fetch_numbers_from_url(url))
    
    unique_numbers = sorted(unique_numbers)  # Sort the numbers in ascending order
    
    return jsonify({"numbers": unique_numbers})

if _name_ == '__main__':
    app.run(host='0.0.0.0', port=8008)
