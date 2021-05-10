def convert_dec_12bit_to_hex_16bit(dec):
    """
    Функция преобразует десятичное значение для 12 bit в hex значение 16 bit
    :param dec: integer
    :return: hex
    """

    if dec not in range(0, 4096):
        raise Exception('The decimal integer should be in range between 0 to 4095')
    tmp = bin(dec)[2:]
    tmp = tmp.zfill(16)
    # return hex(int(tmp, 2))
    four_i = ""
    l = []
    for i in tmp:
        four_i += i
        if len(four_i) == 4:
            l.append(four_i)
            four_i = ""
    return '0x' + ''.join([hex(int(b, 2))[2:] for b in l])


def convert_dec_12bit_to_hex_16bit_2(dec):
    if dec not in range(0, 4096):
        raise Exception('The decimal integer should be in range between 0 to 4095')
    return f"{dec:#0{6}x}"


# тест для функции convert_dec_12bit_to_hex_16bit_2
def test_convert_dec_12bit_to_hex_16bit_2():
    for dec in range(0, 4097):
        assert len(f"{dec:#0{6}x}") == 6
        assert int(f"{dec:#0{6}x}", 16) == dec


if __name__ == "__main__":
    print(convert_dec_12bit_to_hex_16bit(4095))
    print(convert_dec_12bit_to_hex_16bit_2(4095))
