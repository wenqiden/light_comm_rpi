import RPi.GPIO as GPIO
import time

LED_LOW_PIN = 18
LED_HIGH_PIN = 12
ASCII_BITS = 8
START_SIGNAL_DURATION = 1
BIT_INTERVAL = 0.2
CHAR_INTERVAL = 1
TEXT = "HelloWorld"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_LOW_PIN, GPIO.OUT)
GPIO.setup(LED_HIGH_PIN, GPIO.OUT)

def string_to_binary(text):
    return [format(ord(char), '08b') for char in text]

def transmit_start_signal():
    GPIO.output(LED_LOW_PIN, GPIO.HIGH)
    GPIO.output(LED_HIGH_PIN, GPIO.HIGH)
    time.sleep(START_SIGNAL_DURATION)
    GPIO.output(LED_LOW_PIN, GPIO.LOW)
    GPIO.output(LED_HIGH_PIN, GPIO.LOW)
    time.sleep(CHAR_INTERVAL)

def transmit_binary(binary_text, bit_delay=BIT_INTERVAL):
    """Flash LED to transmit binary data."""
    print("Transmitting:", binary_text)
    for bit in binary_text:
        if bit == '1':
            GPIO.output(LED_HIGH_PIN, GPIO.HIGH)
            GPIO.output(LED_LOW_PIN, GPIO.LOW)
        else:
            GPIO.output(LED_LOW_PIN, GPIO.HIGH)
            GPIO.output(LED_HIGH_PIN, GPIO.LOW)
        time.sleep(bit_delay)
    GPIO.output(LED_HIGH_PIN, GPIO.LOW)
    GPIO.output(LED_LOW_PIN, GPIO.LOW)
    time.sleep(CHAR_INTERVAL)

if __name__ == '__main__':
    try:
        binary_text_list = string_to_binary(TEXT)
        for binary_text in binary_text_list:
            transmit_binary(binary_text)
    finally:
        GPIO.cleanup()