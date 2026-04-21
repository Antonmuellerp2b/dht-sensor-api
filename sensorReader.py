import adafruit_dht
import board
import time

# initialize DHT22 sensor
try:
    dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)  # if using Raspberry Pi, set use_pulseio=False
except Exception as e:
    print(f"Error while reading the sensor: {e}")
    dht_device = None

def read():
    """Read temperature and humidity from the DHT22 sensor."""
    if dht_device is None:
        print("Sensor not initialized.")
        return None, None

    for _ in range(10):  # Max. 10 tries to read the sensor
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            if temperature is not None and humidity is not None:
                return temperature, humidity
        except RuntimeError as err:
            print(f"Error reading, next try... ({err})")
            time.sleep(5)  # wait before retrying

    print("Could not read from sensor after 10 attempts.")
    return None, None  # in case of failure, return None values
