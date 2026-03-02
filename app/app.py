from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return {"users": 10}

if __name__ == "__main__":
    app.run(debug=True)
