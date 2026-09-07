number = input("Enter a number: ")
base = input("Enter the base of the number (2, 8, 10, 16): ")
new_base = input("Enter the base to convert to (2, 8, 10, 16): ")

decimal = int(number, int(base))

if new_base == "2":
    result = format(decimal, "b")
elif new_base == "8":
    result = format(decimal, "o")
elif new_base == "10":
    result = format(decimal, "d")
elif new_base == "16":
    result = format(decimal, "X")

print(result)