def convert_dscp_dec_to_tos_hex(dec):
    """
    Функция преобразует десятичное значение для 6-ти битного подполя DSCP ipv4 заголовка
    в hex значение 8 битного поля ToS
    :param dec: integer
    :return: hex
    """
    # if dec not in range(0, 63):
    #     raise Exception('The integer should be in range between 0 to 63')
    # tmp = bin(dec)[2:]
    # while not len(tmp) == 6:
    #     tmp = '0' + tmp
    # while not len(tmp) == 8:
    #     tmp = tmp + '0'
    # return hex(int(tmp, 2))

    if dec not in range(0, 64):
        raise Exception('The decimal integer should be in range between 0 to 63')
    tmp = bin(dec)[2:]
    tmp = tmp.zfill(6)
    tmp = tmp.ljust(8, "0")
    return hex(int(tmp, 2))


def convert_dscp_dec_to_tos_hex_2(dec):
    """
    Функция преобразует десятичное значение для 6-ти битного подполя DSCP ipv4 заголовка
    в hex значение 8 битного поля ToS
    :param dec: integer
    :return: hex
    """

    if dec not in range(0, 64):
        raise Exception('The decimal integer should be in range between 0 to 63')
    return f"{dec << 2:#0{4}x}"


# тест для функции convert_dscp_dec_to_tos_hex_2
def test_convert_dscp_dec_to_tos_hex_2():
    for dec in range(0, 64):
        assert len(f"{dec << 2:#0{4}x}") == 4
        assert int(f"{dec << 2:#0{4}x}", 16) == dec << 2


if __name__ == "__main__":
    print(convert_dscp_dec_to_tos_hex(21))
    print(convert_dscp_dec_to_tos_hex_2(21))

