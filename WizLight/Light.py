import ipaddress

import Communicator


class Light:
    ip = ipaddress.ip_address("0.0.0.0")
    state: bool
    com: Communicator

    def __init__(self, ip: ipaddress.IPv4Address | str):
        if type(ip) is str:
            ip = ipaddress.IPv4Address(ip)
        self.ip = ip
        self.com = Communicator.Communicator()
        self.state = False  # Assumes the light state is False

    def trigger_state(self) -> bool:
        new_state = not self.state
        self.set_state(new_state)
        return new_state

    def set_state(self, state: bool) -> bool:
        self.state = state

        state_msg = {"method": "setState", "params": {"state": state}}
        self.com.send_message(state_msg, self.ip)

        return state

    def get_state(self) -> bool:
        return self.state

    def get_bulb_config(self):
        """Return the configuration from the bulb."""
        resp = self.com.send_message({"method": "getSystemConfig", "params": {}}, self.ip)
        return resp


if __name__ == "__main__":
    import time

    light = Light("10.42.0.175")
    try:
        while True:
            light.trigger_state()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program was interrupted by keyboard, setting light to on before finishing.")
    finally:
        light.set_state(True)
