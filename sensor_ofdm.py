import RPi.GPIO as GPIO
import time

SENSOR_ONE_PIN = 23  # PIN for light sensor
SENSOR_TWO_PIN = 27
ASCII_BITS = 8
START_SIGNAL_DURATION = 5
BIT_DELAY = 0.2
BIT_INTERVAL = 0.1
CHAR_INTERVAL = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_ONE_PIN, GPIO.IN)
GPIO.setup(SENSOR_TWO_PIN, GPIO.IN)

def binary_to_string(binary_text):
    """Convert binary string (8-bit per char, no spaces) back to text."""
    return ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))

def wait_for_start_signal():
    while True:
        if GPIO.input(SENSOR_ONE_PIN) == GPIO.HIGH and GPIO.input(SENSOR_TWO_PIN) == GPIO.HIGH:
            start_time = time.time()
            while GPIO.input(SENSOR_ONE_PIN) == GPIO.HIGH and GPIO.input(SENSOR_TWO_PIN) == GPIO.HIGH:
                if time.time() - start_time >= START_SIGNAL_DURATION * 0.8:
                    print("Start signal detected! Synchronizing...")
                    time.sleep(BIT_DELAY)
                    return
                time.sleep(0.01)
        time.sleep(0.01)

def receive_binary(bit_delay=BIT_DELAY):
    """Read binary data using light sensor."""
    received_bits = ''
    for _ in range(ASCII_BITS // 2):
        bit_one = '1' if GPIO.input(SENSOR_ONE_PIN) == GPIO.HIGH else '0'
        bit_two = '1' if GPIO.input(SENSOR_TWO_PIN) == GPIO.HIGH else '0'
        received_bits += bit_one + bit_two
        time.sleep(bit_delay)  # Wait for next bit
        time.sleep(BIT_INTERVAL)
    print("Received:", received_bits, "=>", binary_to_string(received_bits))
    time.sleep(CHAR_INTERVAL)

if __name__ == '__main__':
    print("Receiving data...")
    try:
        wait_for_start_signal()
        while True:
            receive_binary()
    finally:
        GPIO.cleanup()