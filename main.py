# Simon Rigonato
# COP 3502C
# Group: Simon Rigonato and Cory White

def encode(password):       #new password to be encoded
    encoded_password = []   # creates list with new encoded password
    for digit in password:
        if digit.isdigit():
            encoded_digit = (int(digit) + 3) % 10
            encoded_password.append(str(encoded_digit))
        else:
            raise ValueError("Wrong key.")
    return ''.join(encoded_password)        #joins password

def decode(password):       #new password to be encoded
    encoded_password = []   # creates list with new encoded password
    for digit in password:
        if digit.isdigit():
            encoded_digit = (int(digit) - 3) % 10
            encoded_password.append(str(encoded_digit))
        else:
            raise ValueError("Wrong key.")
    return ''.join(encoded_password)

def menu():    #Menu goes into  main
    print("Menu\n" + "-------------\n" +
          "1. Encode\n" +
          "2. Decode\n" +
          "3. Quit\n")

def main():         #puts everything into main
    while True:
        menu()
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            password = (input("Please enter your password to encode: "))
            encoded_password = encode(password)
            global encoded_password
            print("Your password has been encoded and stored!")  # print above encoded password
        elif menu_choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(password)}")   #One whole function for bove
        else:
            exit(0)


if __name__ == '__main__':
    main()



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


