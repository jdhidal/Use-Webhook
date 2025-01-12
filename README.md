# Webhook en Python

This project is a simple implementation of a webhook in Python using the Flask framework. A webhook is a mechanism that allows an application to send data or notifications to another application when a specific event occurs.

## What is a Webhook?
A **webhook** is an event-driven communication technique. It allows systems to interact in real-time by sending HTTP POST requests to a specific URL when an event happens. Unlike traditional polling methods, webhooks reduce latency and server load by sending data only when necessary.

### Why use Python for a Webhook?
Python is ideal for implementing webhooks due to:
- **Simplicity:** It allows for rapid application development with fewer lines of code.
- **Flexibility:** It has tools and frameworks like Flask that simplify the creation of HTTP endpoints.
- **Compatibility:** Python is widely supported by various services and libraries.

---

## Requiments

1. Python 3.7 or higher installed on your machine.
2. Dependencies:
    - Flask (installable via `pip`).

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/tu-repositorio/webhook-python.git
    cd Use-Webhook
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```
    You should see a message like:
    ```
    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    ```

2. The application is now listening on `http://localhost:5000/webhook` for POST requests.

3. To send an event to the webhook, use the following **curl** command (compatible with Windows CMD):
    ```cmd
    curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"Hola Mundo\"}" http://localhost:5000/webhook
    ```

    **Expected result:**
    - In the terminal where you ran app.py, you should see:
      ```
      Message received: Hello World
      ```
    - La respuesta del servidor será:
      ```json
      {
          "response": "Message received successfully: Hello World"
      }
      ```

---
