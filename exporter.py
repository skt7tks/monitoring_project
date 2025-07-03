from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import requests
import time

app = Flask(__name__)

# Prometheus metric-ები
RESPONSE_TIME = Gauge('website_response_time_seconds', 'Website Response Time')
STATUS_CODE = Gauge('website_status_code', 'Website HTTP Status Code')

# აქ ჩასვი მონიტორინგის საიტის URL
URL = 'https://google.com'

@app.route('/metrics')
def metrics():
    start = time.time()
    try:
        response = requests.get(URL, timeout=5)
        elapsed = time.time() - start
        RESPONSE_TIME.set(elapsed)
        STATUS_CODE.set(response.status_code)
    except Exception as e:
        RESPONSE_TIME.set(10.0)
        STATUS_CODE.set(0)

    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
