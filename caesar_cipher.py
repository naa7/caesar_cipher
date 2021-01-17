def caesar_encrypt(clear_text):
    encrypted_output = ""
    # flag = 0
    
    for i in range(len(clear_text)):
        
        """
        if clear_text[i].isupper():
            flag = 1
            clear_text[i] = clear_text[i].lower()
        elif clear_text[i] == ' ':
            encrypted_output = encrypted_output + "#"
            continue
        elif clear_text[i] == '?':
            encrypted_output = encrypted_output + "!"
            continue
        elif clear_text[i] == '!':
            encrypted_output = encrypted_output + "?"
            continue
        """
        
        char_position = ord(clear_text[i])
        #char_position = char_position - 97
        new_char_position = char_position + 3

        # To use only use letters, uncomment next 2 lines
	    # new_char_position = new_char_position % 26
        #new_char_position = new_char_position + 97
        new_char = chr(new_char_position)
        
        # if flag == 1:
        #   new_char =  new_char.upper()
        
        encrypted_output = encrypted_output + new_char
        # flag = 0

    print("---------------")
    print("Encrypted text:", encrypted_output)


def caesar_decrypt(cipher_text):
    decrypted_output = ""
    # flag = 0
    
    for i in range(len(cipher_text)):

        """
        if cipher_text[i].isupper():
            flag = 1
            cipher_text[i] = cipher_text[i].lower()
	    elif cipher_text[i] == ' ':
            decrypted_output = decrypted_output + "#"
            continue
        elif cipher_text[i] == '?':
            decrypted_output = decrypted_output + "!"
            continue
        elif cipher_text[i] == '!':
            decrypted_output = decrypted_output + "?"
            continue
        """
        
        char_position = ord(cipher_text[i])
        # char_position = char_position - 97
        new_char_position = char_position - 3
        # new_char_position = new_char_position % 26
        # new_char_position = new_char_position + 97
        new_char = chr(new_char_position)
        
        # if flag == 1:
        #   new_char = new_char.upper()

        decrypted_output = decrypted_output + new_char
        # flag = 0

    print("---------------")
    print("Decrypted text:", decrypted_output)


def main():
    try:
        print("#######################")
        print("###  Caesar Cipher  ###")
        print("#######################")

        while True:
            choice = input("Do you want to encrypt or decrypt text?[E/d]: ")
            print("-----------------------------------------------")
            if choice == 'E' or choice == 'e':
                clear_text = list(input("Enter text to be encrypted: "))
                caesar_encrypt(clear_text)
            elif choice == 'D' or choice == 'd':
                cipher_text = list(input("Enter text to be decrypted: "))
                caesar_decrypt(cipher_text)
            else:
                print("Error, Entry is not recognized!")
                return 1
            print("-----------------------------------------------")
            answer = input("Do you want to quit?[Y/n]: ")
            if answer == 'N' or answer == 'n':
                continue
            else:
                print("########################")
                print("###  End of Program  ###")
                print("########################")
                break
    except:
        print("\nError, Program Exit!") 

if __name__ == "__main__":
    main()




