# Graham Johnston

def decoder(password):
    decoded_password = ''

    for d in password:
        deco_digit = int(d) - 3
        if deco_digit <= 0:
            deco_digit += 10

        decoded_password += str(deco_digit)

    print(f'The encoded password is {password}, and the original password is {decoded_password}.')
