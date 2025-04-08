import RPi.GPIO as GPIO
import time

LED_ONE_PIN = 18
LED_TWO_PIN = 12
ASCII_BITS = 8
START_SIGNAL_DURATION = 5
BIT_DELAY = 0.2
BIT_INTERVAL = 0.1
CHAR_INTERVAL = 1
TEXT = "HelloWorld"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ONE_PIN, GPIO.OUT)
GPIO.setup(LED_TWO_PIN, GPIO.OUT)

def string_to_binary(text):
    return [format(ord(char), '08b') for char in text]

def transmit_start_signal():
    GPIO.output(LED_ONE_PIN, GPIO.HIGH)
    GPIO.output(LED_TWO_PIN, GPIO.HIGH)
    time.sleep(START_SIGNAL_DURATION)
    GPIO.output(LED_ONE_PIN, GPIO.LOW)
    GPIO.output(LED_TWO_PIN, GPIO.LOW)
    time.sleep(CHAR_INTERVAL)

def transmit_binary(binary_text):
    """Flash LED to transmit binary data."""
    print("Transmitting:", binary_text)
    for i in range(0, len(binary_text), 2):
        bit1 = binary_text[i]
        bit2 = binary_text[i + 1]
        GPIO.output(LED_ONE_PIN, GPIO.HIGH if bit1 == '1' else GPIO.LOW)
        GPIO.output(LED_TWO_PIN, GPIO.HIGH if bit2 == '1' else GPIO.LOW)
        time.sleep(BIT_DELAY)
        # Turn off LEDs after each 2-bit symbol for a short interval to avoid overlap
        GPIO.output(LED_ONE_PIN, GPIO.LOW)
        GPIO.output(LED_TWO_PIN, GPIO.LOW)
        time.sleep(BIT_INTERVAL)
    time.sleep(CHAR_INTERVAL)

if __name__ == '__main__':
    try:
        binary_text_list = string_to_binary(TEXT)
        transmit_start_signal()
        for binary_text in binary_text_list:
            transmit_binary(binary_text)
    finally:
        GPIO.cleanup()