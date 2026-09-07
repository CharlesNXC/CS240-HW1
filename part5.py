def test_converter():
    # Zero
    number = 0
    print("Zero:")
    print("Decimal:", number)
    print("Binary:", format(number, "08b"))
    print()

    # Largest unsigned 8-bit value
    number = 255
    print("Largest unsigned value:")
    print("Decimal:", number)
    print("Binary:", format(number, "08b"))
    print("Octal:", format(number, "o"))
    print("Hexadecimal:", format(number, "X"))
    print()

    # Negative two's-complement value
    number = -1
    twos_complement = format(number & 0xFF, "08b")

    print("Negative two's-complement value:")
    print("Decimal:", number)
    print("8-bit binary:", twos_complement)


test_converter()