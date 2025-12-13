from flask import Flask, jsonify 
import os 
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return jsonify({"message": "My Cloud Backend", "status": "running"}) 
 
@app.route('/health') 
def health(): 
    return jsonify({"status": "healthy"}), 200 
 
if __name__ == '__main__': 
    port = int(os.getenv("PORT", 3000)) 
    app.run(host="0.0.0.0", port=port) 
