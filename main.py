# import Discovery
# import Light
import RPi.GPIO as GPIO

GPIO_PIN: int = 16


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        if GPIO.input(GPIO_PIN) == GPIO.HIGH:
            print("Button was pushed!")


if __name__ == "__main__":
    main()
