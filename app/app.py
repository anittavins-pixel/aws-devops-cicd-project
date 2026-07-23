from flask import Flask

print("Starting Flask...")

app = Flask(__name__)

@app.route("/")
def home():
    return "AWS DevOps CI/CD Project Running"

if __name__ == "__main__":
    print("Running server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
