# Graham Johnston

def decoder(password):
    decoded_password = ''.join(str((int(d) - 3) % 10) for d in password)

    return decoded_password
