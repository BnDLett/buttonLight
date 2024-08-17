import ipaddress
from Communicator import Communicator
from Light import Light


class Discovery:
    results = []
    com: Communicator

    def __init__(self, subnet_ip: ipaddress.IPv4Address = ipaddress.IPv4Address("192.168.1.0")):
        """
        Discover lights on the local network. It will not return a value, but rather instead it will append the results
        to a list that you can access with the get_lights() method.
        :param subnet_ip: The IP subnet to check (example: 192.168.10.0; will check 192.168.10.x).
        """
        self.discover(subnet_ip)
        self.com = Communicator()

    def discover(self, subnet_ip: ipaddress.IPv4Address = ipaddress.IPv4Address("192.168.1.0")):
        """
        Discover for any lights on the local network. This is initially ran by the constructor, but can be run again.
        :param subnet_ip: The IP subnet to check (example: 192.168.10.0; will check 192.168.10.x).
        :return: None; access results with the get_lights() method.
        """
        list_ip = subnet_ip.__format__("").split(".")
        self.results = []

        for i in range(254):
            list_ip[3] = str(i + 1)

            # I was going to use threads to speed up the process, but I didn't feel like dealing with the troubles of
            # multiprocessing today.

            # thread_pool.append(threading.Thread(target=self.check_light, args=[ipaddress.
            #                                                                    IPv4Address(".".join(list_ip)),]))
            # thread_pool[i].start()

            ip = ipaddress.IPv4Address(".".join(list_ip))
            result = self.__check_light(ip)
            if result is None:
                continue

            light = Light(ip)
            self.results.append(light)

    @staticmethod
    def __check_light(subnet_ip: ipaddress.IPv4Address = ipaddress.IPv4Address("192.168.1.0")):
        com = Communicator()
        result = com.send_message({}, subnet_ip)
        return result

    def get_lights(self):
        """
        Returns the lights found with the discover method.
        :return: A list containing :class:`Light` objects.
        """
        return self.results


if __name__ == "__main__":
    disc = Discovery(ipaddress.IPv4Address("10.42.0.0"))
    print(disc.get_lights()[0].ip)

