str = "1010"

def to_decimal(num_string, base):
    # Turn the string into a list of individual characters
    digit_list = list(num_string)

    # Reverse the string to look at each character in the correct order
    digit_list.reverse()

    value = 0

    for i in range(len(digit_list)):
        print(f"{int(digit_list[i])} in the {base ** i}'s place' ")
        value += int(digit_list[i]) * (base ** i)

    print(f"The final number is {value}")


to_decimal(str, 2)

