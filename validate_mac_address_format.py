import re


def validate_mac_address_format(value: str):
    regex = r"^(?P<p_1>\w{2}):(?P<p_2>\w{2}):(?P<p_3>\w{2}):(?P<p_4>\w{2}):(?P<p_5>\w{2}):(?P<p_6>\w{2})"
    match = re.search(regex, value)
    if match:
        return match.groupdict()


def validate_mac_address_parts(parts: dict):
    validate_parts = all(list(map(lambda x: hex(int(x, 16)), parts.values())))
    return validate_parts


def validate_mac_address(value: str):
    validate_parts = validate_mac_address_format(value)
    if not validate_parts:
        raise Exception("MAC-address should be set in format 'xx:xx:xx:xx:xx:xx'")
    try:
        validate_mac_address_parts(validate_parts)
    except ValueError as e:
        raise Exception(f"Invalid MAC-address: {str(e)}")
    return validate_parts


mac = 'ce:22:a5:5a:1m:24'
print(validate_mac_address(mac))
