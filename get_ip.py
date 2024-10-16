import psutil
import netaddr
from psutil import net_if_addrs
from netaddr import IPAddress


def get_ip():
    scan = psutil.net_if_addrs()
    wifi = (scan["Wi-Fi"])
    mask = IPAddress(wifi[1].netmask).netmask_bits()
    addresses = pow(2,(32-mask))
    print(wifi[1].address + "/" +  str(mask))
    print(str(addresses) + " adresses")


if __name__ == "__main__":
    get_ip()