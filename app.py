from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for the webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get data from the request body
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "Field 'message' not found"}), 400

    # Process the message
    message = data['message']
    print(f"Message received: {message}")

    # Respond to the client
    return jsonify({"response": f"Message received successfully: {message}"}), 200

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000)
