def check_bit4(input):
    mask = 0b1000
    if input & mask:
        return "on"
    return "off"
