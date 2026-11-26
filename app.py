# Flask small web framework
from flask import Flask
import logging
# Automatically exposes metrics at /metrics ( used in module 8)
from prometheus_flask_exporter import PrometheusMetrics

# Show time and severity in log lines
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
app = Flask(__name__)
metrics = PrometheusMetrics(app) # adds /metrics endpoint

@app.route('/')
def hello():
    logging.info("Home page requested")
    return "Hello DevOps!, 2026 Its devops team"

@app.route('/health')
def health():
    #Monitoring tools call this to check the app is alive 
    return {"status":"OK"},200

# A plain fuction so we can show a simple unit test
def add(a,b):
    return a+b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)