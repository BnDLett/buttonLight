import ipaddress
import json
import socket
from typing import SupportsIndex


class Communicator:
    PORT = 38899

    def __init__(self):
        self.sock = socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, msg: dict, destination: ipaddress.IPv4Address):
        if type(destination) is ipaddress.IPv4Address:
            destination = destination.__format__("")

        self.sock.settimeout(0.05)

        it = json.dumps(msg)
        data = json.dumps(msg).encode()
        self.sock.connect((destination, self.PORT))
        self.sock.sendall(data)

        try:
            result = self.sock.recv(1024)
        except ConnectionRefusedError:
            return None
        except TimeoutError:
            return None

        return result.decode()


if __name__ == "__main__":
    com = Communicator()
    state_msg = {"method": "setState", "params": {"state": True}}
    com.send_message(state_msg, ipaddress.IPv4Address("192.168.10.127"))
