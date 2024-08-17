# import Discovery
# import Light
import RPi.GPIO as GPIO

GPIO_PIN: int = 16


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")
