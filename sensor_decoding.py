import RPi.GPIO as GPIO
import time

SENSOR_PIN = 23  # PIN for light sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def binary_to_string(binary_text):
    """Convert binary string (8-bit per char, no spaces) back to text."""
    return ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))

def receive_binary(expected_bits, bit_delay=0.2):
    """Read binary data using light sensor."""
    received_bits = ""
    print("Receiving data...")
    for _ in range(expected_bits):
        bit = '1' if GPIO.input(SENSOR_PIN) == GPIO.HIGH else '0'
        received_bits += bit
        time.sleep(bit_delay)  # Wait for next bit
    return received_bits

if __name__ == '__main__':
    try:
        received_bits = receive_binary(len("HelloWorld")*8)
        print("Received:", binary_to_string(received_bits))
    finally:
        GPIO.cleanup()