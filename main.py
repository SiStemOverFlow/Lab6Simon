# Simon Rigonato
# COP 3502C
# Group: Simon Rigonato and Cory White

def encode(password):
    encoded_password = ""
    for digit in password:
        if digit.isdigit():
            encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    else:
        encoded_password+= digit
    print("Your password has been encoded and stored!")
    print(encoded_password + "\n")
    return encoded_password
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        if digit.isdigit():
            decoded_digit = (int(digit) - 3) % 10
            decoded_password += str(decoded_digit)
        else:
            decoded_password += digit
    print("The encoded password is" + encoded_password +
          ", and the original password is "+ decoded_password)

def menu():
    print("Menu\n" + "-------------\n" +
          "1. Encode\n" +
          "2. Decode\n" +
          "3. Quit\n")


while True:
    menu()
    menu_choice = int(input("Please enter an option: "))
    if menu_choice == 1:
        password = int(input("Please enter your password to encode: "))
        encoded_password = encode(password)
    elif menu_choice == 2:
        decode(encoded_password)

    else:
        exit(0)







# if __name__ == '__main__':
    # menu()
    # menu_choice = int(input("Please enter an option: "))
    # if menu_choice == 1:
    #     password = int(input("Please enter your password to encode: "))
    #     encode(password)
    #
    # elif menu_choice == 2:
    #     decode(encoded_password)
    #
    # else:
    #     exit(0)


