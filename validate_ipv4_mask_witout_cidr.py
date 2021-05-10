import re

from ipaddress import AddressValueError, IPv4Address


def _check_hwaddress(mac_address):
    # mac_address_re = "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
    mac_address_re = "([0-9a-f]{2}:){5}[0-9a-f]{2}$"
    if not re.match(mac_address_re, mac_address.lower()):
        error = '{} mac-address is invalid. Should set mac-address in format xx:xx:xx:xx:xx:xx\n'.format(mac_address)
        return False, error
    return True, None


def _validate_args(ipv4_address, ipv4_netmask, ipv4_gateway, mac_address=None):
    errors = []

    # 1
    if mac_address:
        check_result, error = _check_hwaddress(mac_address)
        if not check_result:
            errors.append(error)
    # 2
    try:
        IPv4Address(ipv4_address)
    except AddressValueError:
        errors.append(f"{ipv4_address} ip-address is invalid.\n")
    # 3
    try:
        IPv4Address(ipv4_gateway)
    except AddressValueError:
        errors.append(f"{ipv4_gateway} gateway address is invalid.\n")

    if not errors:
        # 4
        if len(ipv4_netmask.split(".")) != 4:
            errors.append(f"{ipv4_netmask} network mask should be in format xxx.xxx.xxx.xxx.\n")

        # 5
        if not ipv4_netmask.replace(".", "").isdigit():
            errors.append(f"{ipv4_netmask} network mask should consist only digits.\n")

        bin_mask = "".join(f"{int(octet):08b}" for octet in ipv4_netmask.split("."))

        # 6
        if len(bin_mask) != 32:
            errors.append(f"Every {ipv4_netmask} network mask octet should be in range from 0 to 255.\n")

        # 7
        match = re.fullmatch(r"1+0+", bin_mask)
        if not match:
            errors.append(f"{ipv4_netmask} network mask bits shouldn't be start from zero and 1 bits shouldn't "
                          f"been interrupted zero bits.\n")

        bin_address = "".join(f"{int(octet):08b}" for octet in ipv4_address.split("."))
        net_number = bin_mask.count("1")
        bin_network_address = bin_address[0:net_number].ljust(32, "0")
        bin_broadcast_network_address = bin_address[0:net_number].ljust(32, "1")
        bin_gateway = "".join(f"{int(octet):08b}" for octet in ipv4_gateway.split("."))
        network_address = []
        ip_octet = ""
        for i in bin_network_address:
            ip_octet += i
            if len(ip_octet) == 8:
                network_address.append(str(int(ip_octet, 2)))
                ip_octet = ""
        str_network_address = ".".join(network_address)

        # 8
        # не включачем в проверку network адрес и broadcast адрес
        if int(bin_gateway, 2) not in range(int(bin_network_address, 2) + 1, int(bin_broadcast_network_address, 2)):
            errors.append(f"{ipv4_gateway} gateway address is out of {str_network_address} network's "
                          f"addresses scope.\n")

        # 9
        if bin_address == bin_gateway:
            errors.append(f"{ipv4_address} ip-address and {ipv4_gateway} gateway shouldn't be the same.\n")
    if errors:
        print(''.join(errors))
        return False
    return True


if __name__ == "__main__":
    data = dict(
                ipv4_address='192.168.20.120',
                ipv4_netmask='255.255.255.252',
                ipv4_gateway='192.168.20.121',
                mac_address='00:00:00:00:00:00')
    result = _validate_args(**data)
