def to_roman(data):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]

    return t + h + te + o


def to_arab(data):
    base = "I" * data

    base = base.replace("I" * 5, "V")
    base = base.replace("V" * 2, "X")
    base = base.replace("X" * 5, "L")
    base = base.replace("L" * 2, "C")
    base = base.replace("C" * 5, "D")
    base = base.replace("D" * 2, "M")

    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")

    return base



print(to_roman(1234))
print(to_arab(str(MMMX)))