from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Define GPIO pins for devices
LIGHT_PIN = 17
FAN_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)

@app.route('/control', methods=['POST'])
def control_device():
    device = request.json.get("device")
    action = request.json.get("action")

    if device == "light":
        GPIO.output(LIGHT_PIN, GPIO.HIGH if action == "on" else GPIO.LOW)
    elif device == "fan":
        GPIO.output(FAN_PIN, GPIO.HIGH if action == "on" else GPIO.LOW)
    else:
        return {"message": "Invalid device"}, 400

    return {"message": f"{device} turned {action}"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)