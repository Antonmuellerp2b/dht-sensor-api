from flask import Flask, jsonify
from sensorReader import read

# create Flask-App
app = Flask(__name__)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    """Returns the current temperature and humidity readings from the DHT22 sensor."""
    temperature, humidity = read()
    
    if temperature is None or humidity is None:
        return jsonify({'error': 'Error reading sensor data.'}), 500

    return jsonify({'temperature': temperature, 'humidity': humidity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
