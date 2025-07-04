from flask import Flask, Response
from prometheus_client import Gauge, Counter, generate_latest
import requests
import time

app = Flask(__name__)


URLS = [
    'https://google.com',
    'https://yahoo.com'
]


RESPONSE_TIME = {}
STATUS_CODE = {}
ERROR_COUNT = {}
LATENCY_ALERT = {}

LATENCY_THRESHOLD = 2.0  

for url in URLS:
    url_label = url.replace("https://", "").replace(".", "_").replace("/", "_")
    RESPONSE_TIME[url] = Gauge(f'website_response_time_seconds_{url_label}', f'Website Response Time for {url}')
    STATUS_CODE[url] = Gauge(f'website_status_code_{url_label}', f'HTTP Status Code for {url}')
    ERROR_COUNT[url] = Counter(f'website_error_count_{url_label}', f'Number of request errors for {url}')
    LATENCY_ALERT[url] = Gauge(f'website_latency_alert_{url_label}', f'Latency Alert for {url} (1 = high latency)')

@app.route('/metrics')
def metrics():
    for url in URLS:
        start = time.time()
        try:
            response = requests.get(url, timeout=5)
            elapsed = time.time() - start

            RESPONSE_TIME[url].set(elapsed)
            STATUS_CODE[url].set(response.status_code)

            if elapsed > LATENCY_THRESHOLD:
                LATENCY_ALERT[url].set(1)
                print(f"⚠️ High latency detected for {url}: {elapsed:.3f} seconds")
            else:
                LATENCY_ALERT[url].set(0)

            print(f"✅ {url} responded in {elapsed:.3f} seconds with status {response.status_code}")

        except Exception as e:
            RESPONSE_TIME[url].set(10.0)
            STATUS_CODE[url].set(0)
            LATENCY_ALERT[url].set(1)
            ERROR_COUNT[url].inc()
            print(f"❌ Error requesting {url}: {str(e)}")

    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
