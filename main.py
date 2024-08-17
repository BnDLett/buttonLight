# import Discovery
# import Light
import RPi.GPIO as GPIO


def get_pin_number() -> int:
    """
    Gets the pin number from the user's input.
    :return: integer representing the pin number
    """
    try:
        pin_number = input("Type in the pin that the button uses:\n> ")
        int(pin_number)
    except ValueError:
        print("The value typed in was not able to be converted into an integer. Ensure that you've typed it correctly.")
        get_pin_number()


def button_callback():
    print("Button was pushed!")


def main(pin_number: int):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(pin_number, GPIO.RISING, callback=button_callback())

    input("Press enter to kill the program.")
    GPIO.cleanup()


if __name__ == "__main__":
    GPIO_PIN_NUMBER: int = get_pin_number()
    main(GPIO_PIN_NUMBER)
