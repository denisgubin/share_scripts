import re
from ipaddress import IPv4Network, AddressValueError, NetmaskValueError


def validate_ipv4_network_format(pattern: str):
    regex = r"^(?P<ipv4_address>(\d{1,3}\.){3}\d{1,3})/(?P<network_number>\d{1,2})$"
    match = re.search(regex, pattern)
    if match:
        res = match.groupdict()
        return res


def validate_ipv4_network_cidr(value: str):
    if not validate_ipv4_network_format(value):
        raise Exception("IPv4 network should be set in format 'xxx.xxx.xxx.xxx/xx'")
    try:
        IPv4Network(value)
    except AddressValueError as e:
        raise Exception(f"Invalid IPv4 address: {str(e)}")
    except NetmaskValueError as e:
        raise Exception(f"Invalid IPv4 netmask: {str(e)}")
    return True



ip_address = '192.168.1.22/234'
print(validate_ipv4_network_cidr(ip_address))
