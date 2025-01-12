from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para el webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtener datos del cuerpo de la solicitud
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "No se encontró el campo 'message'"}), 400

    # Procesar el mensaje
    message = data['message']
    print(f"Mensaje recibido: {message}")

    # Responder al cliente
    return jsonify({"response": f"Mensaje recibido correctamente: {message}"}), 200

if __name__ == '__main__':
    # Ejecutar el servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
