#Varvara Folimonova
def encode():
    to_encode = input("Please enter your password to encode: ")
    encoded = ""
    for digit in to_encode:
        encoded += str(int(digit)+3)[-1]
    print("Your password has been encoded and stored!")
    return encoded

#Varvara Folimonova
def main():
    while True:
        option = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if option == "1":
            encoded_pass = encode()
        if option == "2":
            pass
        if option == "3":
            break

if __name__ == "__main__":
    main()