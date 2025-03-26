import RPi.GPIO as GPIO
import time

LED_PIN = 18        # Pin for LED output
TEXT = "HelloWorld"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def string_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def transmit_binary(binary_text, bit_delay=0.2):
    """Flash LED to transmit binary data."""
    print("Transmitting:", binary_text)
    for bit in binary_text:
        if bit == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(bit_delay)
    GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == '__main__':
    try:
        binary_text = string_to_binary(TEXT)
        transmit_binary(binary_text)
    finally:
        GPIO.cleanup()