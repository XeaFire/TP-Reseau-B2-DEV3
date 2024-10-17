import psutil
import netaddr
from psutil import net_if_addrs
from netaddr import IPAddress
import os

if os.name == 'nt':
    oswifi = "Wi-Fi"
elif os.name == 'posix':
    oswifi = "System enp0s3"

def function_get_ip():
    scan = psutil.net_if_addrs()
    
    wifi = (scan[oswifi])
    mask = IPAddress(wifi[1].netmask).netmask_bits()
    addresses = pow(2,(32-mask))
    print(wifi[1].address + "/" +  str(mask))
    print(str(addresses) + " adresses")
    return "Command ip called successfully"

if __name__ == "__main__":
    function_get_ip()