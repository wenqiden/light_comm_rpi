import RPi.GPIO as GPIO
import time

LED_PIN = 18        # Pin for LED output
ASCII_BITS = 8
START_SIGNAL_DURATION = 5
BIT_DELAY = 0.2
CHAR_INTERVAL = 1
TEXT = "HelloWorld"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def string_to_binary(text):
    return [format(ord(char), '08b') for char in text]

def transmit_start_signal():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(START_SIGNAL_DURATION)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(CHAR_INTERVAL)

def transmit_binary(binary_text):
    """Flash LED to transmit binary data."""
    print("Transmitting:", binary_text)
    for bit in binary_text:
        if bit == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(BIT_DELAY)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(CHAR_INTERVAL)

if __name__ == '__main__':
    try:
        binary_text_list = string_to_binary(TEXT)
        transmit_start_signal()
        for binary_text in binary_text_list:
            transmit_binary(binary_text)
    finally:
        GPIO.cleanup()