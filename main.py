# import Discovery
# import Light
import RPi.GPIO as GPIO
import ipaddress

from Discovery import Discovery
from Light import Light
from exceptions import LightNotFound

BOUNCE_BACK_TIME: int = 1000


def get_pin_number() -> int:
    """
    Gets the pin number from the user's input.
    :return: integer representing the pin number
    """
    pin_number: int = 0
    try:
        pin_number_str = input("Type in the pin that the button uses:\n> ")
        pin_number = int(pin_number_str)
    except ValueError:
        print("The value typed in was not able to be converted into an integer. Ensure that you've typed it correctly.")
        get_pin_number()

    return pin_number


def button_callback(light: Light):
    light.trigger_state()


def main(pin_number: int, light: Light):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(pin_number, GPIO.RISING, lambda: button_callback(light), BOUNCE_BACK_TIME)

    input("Press enter to kill the program.")
    GPIO.cleanup()


if __name__ == "__main__":
    discoverer = Discovery(ipaddress.IPv4Address("10.42.0.0"))
    lights = discoverer.get_lights()

    print(lights[0].get_state())

    if len(lights == 0):
        raise LightNotFound("Light was NOT found.")

    GPIO_PIN_NUMBER: int = get_pin_number()
    main(GPIO_PIN_NUMBER, lights[0])
