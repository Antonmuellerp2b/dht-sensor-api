from flask import Flask, jsonify
from sensorReader import auslesen

# Flask-App erstellen
app = Flask(__name__)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    """Gibt Temperatur und Luftfeuchtigkeit als JSON zurück."""
    temperature, humidity = auslesen()
    
    if temperature is None or humidity is None:
        return jsonify({'error': 'Fehler beim Abrufen der Sensordaten'}), 500

    return jsonify({'temperature': temperature, 'humidity': humidity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)