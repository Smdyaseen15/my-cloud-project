from flask import Flask
import logging

app = Flask(__name__)

# LOG TO BOTH FILE AND CONSOLE
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

app.logger.addHandler(file_handler)

@app.route("/")
def home():
    app.logger.info("Home API called")
    return {"message": "Backend is working on Ubuntu & EC2!"}

@app.route("/test")
def test():
    app.logger.info("Test API called")
    return {"message": "Log testing successful"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
