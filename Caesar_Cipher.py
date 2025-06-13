letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
          's','t','u','v','w','x','y','z']

#if decrypt shift_key = shift_key * -1 (for one function encrypt & decrypt)
def encryption(plain_msg,shift_key):
    cipher_msg = " "
    for char in plain_msg:
        if char in letter:
            position=letter.index(char)
            new_pos = (position+shift_key)%26
            cipher_msg += letter[new_pos]
        else:
            cipher_msg += char
    print(f"After encryption, message is :\n{cipher_msg}")


def decryption(cipher_msg,shift_key):
    plain_msg = " "
    for char in cipher_msg:
        if char in letter:
            position = letter.index(char)
            new_pos = (position-shift_key)%26
            plain_msg += letter[new_pos]
        else:
            plain_msg += char
    print(f"After decryption, message is:\n{plain_msg}")


end_game = False
while not end_game:
    message_style=input("Enter 'encrypt' for encryption & Enter 'decrypt' for decryption:\n")
    message = input("Enter your message: ").lower()
    shift = int(input("Enter shift key: \n"))

    if message_style == 'encrypt':
        encryption(plain_msg=message,shift_key=shift)

    elif message_style == 'decrypt':
        decryption(cipher_msg=message,shift_key=shift)


    play_game = input("'yes' to continue or 'no' to exit\n")
    if play_game == 'yes':
        end_game = False
    elif play_game == 'no':
        end_game = True
        print("Thank YOU!")