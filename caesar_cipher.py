import subprocess

def caesar_encrypt(clear_text,key):
    encrypted_output = ""
    # flag = 0
    
    for i in range(len(clear_text)):
         
        char_position = ord(clear_text[i])
        #char_position = char_position - 97
        new_char_position = char_position + key

        # To use only use letters, uncomment next 2 lines
        # new_char_position = new_char_position % 26
        #new_char_position = new_char_position + 97
        new_char = chr(new_char_position)
        
        # if flag == 1:
        #   new_char =  new_char.upper()
        
        encrypted_output = encrypted_output + new_char
        # flag = 0

    print("###################")
    print("### Encrypted text:", encrypted_output)
    print("###################")

def caesar_decrypt(cipher_text,key):
    decrypted_output = ""
    # flag = 0
    
    for i in range(len(cipher_text)):

        char_position = ord(cipher_text[i])
        # char_position = char_position - 97
        new_char_position = char_position - key
        # new_char_position = new_char_position % 26
        # new_char_position = new_char_position + 97
        new_char = chr(new_char_position)
        
        # if flag == 1:
        #   new_char = new_char.upper()

        decrypted_output = decrypted_output + new_char
        # fl ag = 0

    print("###################")
    print("### Decrypted text:", decrypted_output)
    print("###################")

def main():
    try:
        #print("#######################")
        #print("###  Caesar Cipher  ###")
        #print("#######################")

        input = subprocess.Popen('zenity --forms --title="Caesar Cipher" --text="" --add-combo="Options"\
                --combo-values="Encrypt|Decrypt" --add-combo="Cipher shifting key" --combo-values="1|2|3|4|5|6|7|8|9" --add-entry="Enter text"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        input = input.stdout.readline()
        input = input.strip()
        option = ""
        text = ""
        key = ""
        for i in range(len(input)):
            if i <= 7:
                if i < 7:
                    option = option + input[i]
                else:
                    continue
            elif i == 8:
                    key = input[i]
            else:
                if input[i] == '|':
                    continue
                else:
                    text = text + input[i]
        if option == "Encrypt" and text != "":
            caesar_encrypt(text,int(key))
        elif option == "Decrypt" and text != "":
            caesar_decrypt(text,int(key))
        else:
            print("#############################")
            print("### Error, Entry missing! ###")
            print("#############################")
            return 1

        """
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
        """

    except:
        print("\nError, Program Exit!") 

if __name__ == "__main__":
    main()




