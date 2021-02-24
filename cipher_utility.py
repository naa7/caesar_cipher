import subprocess

def main():
    try:

        input = subprocess.Popen('zenity --forms --title="Cipher Utility" --text="" --add-combo="Cipher type"\
                --combo-values="Caesar Cipher|ROT Cipher" --add-combo="Options" --combo-values="Encrypt|Decrypt" --add-combo="Cipher shifting key" --combo-values="1|2|3|4|5|6|7|8|9|10|11|12|13|14|15" --add-entry="Enter text"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        input = input.stdout.readline()
        input = input.strip()
        ind = index_list(input,'|')
        cipher = input[:ind[0]]
        option = input[ind[0]+1:ind[1]]
        key = input[ind[1]+1:ind[2]]
        text = input[ind[2]+1:]

        if option == "Encrypt" and text != "":
            if cipher == "Caesar Cipher":
               output1 = caesar_encrypt(text,int(key))
            else:
               output1 = ROT_encrypt(text,int(key))
            output2 = 'echo "' + output1 + '" >> temp.txt && cat temp.txt | zenity --width=400 --height=150 --title="Encrypted Text" --text-info && rm temp.txt'
        
        elif option == "Decrypt" and text != "":
            if cipher == "Caesar Cipher":
               output1 = caesar_decrypt(text,int(key))
            else:
               output1 = ROT_decrypt(text,int(key))
            output2 = 'echo "' + output1 + '" >> temp.txt && cat temp.txt | zenity --width=400 --height=150 --title="Decrypted Text" --text-info && rm temp.txt'
        else:
            print("#############################")
            print("### Error, Entry missing! ###")
            print("#############################")
            return 1
        call = subprocess.call(output2, shell=True)


    except Exception as e:
        print(e)
        print("Error, Program Exit!") 


def index_list(input,item):
    start_at = -1
    indexes = []
    while True:
        try:
            index = input.index(item,start_at+1)
        except ValueError:
            break
        else:
            indexes.append(index)
            start_at = index
    return indexes


def caesar_encrypt(clear_text,key):
    encrypted_output = ""
    for i in range(len(clear_text)):
        #Obtain the ASCII value using ord
        char_position = ord(clear_text[i])
        new_char_position = char_position + key
        if new_char_position > 126:
           new_char_position = new_char_position - 94
        new_char = chr(new_char_position)
        encrypted_output = encrypted_output + new_char

    #print("###################")
    #print("### Encrypted text:", encrypted_output)
    #print("###################")
    return encrypted_output


def caesar_decrypt(cipher_text,key):
    decrypted_output = ""
    for i in range(len(cipher_text)):
        char_position = ord(cipher_text[i])
        new_char_position = char_position - key
        if new_char_position < 32:
           new_char_position = new_char_position + 94
        new_char = chr(new_char_position)
        decrypted_output = decrypted_output + new_char

    #print("###################")
    #print("### Decrypted text:", decrypted_output)
    #print("###################")
    return decrypted_output


def ROT_encrypt(clear_text,key):
    encrypted_output = ""
    flag = 0

    for i in range(len(clear_text)):
       letter = clear_text[i]
       if letter.isupper() == True:
          letter = letter.lower()
          flag = 1
       char_position = ord(letter)
       if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):
          encrypted_output = encrypted_output + chr(char_position)
          continue
       char_position = char_position - 97
       new_char_position = char_position + key
       # works the same as 97 and modulu 26
       new_char_position = new_char_position % 26
       new_char_position = new_char_position + 97
       new_char = chr(new_char_position)
       if flag == 1:
          new_char = new_char.upper()
          flag = 0
       encrypted_output = encrypted_output + new_char

#    print("###################")
#    print("### Encrypted text:", encrypted_output)
#    print("###################")
    return encrypted_output

def ROT_decrypt(cipher_text,key):
    decrypted_output = ""

    for i in range(len(cipher_text)):
       letter = cipher_text[i]
       if letter.isupper() == True:
          letter = letter.lower()
          flag = 1
       char_position = ord(letter)
       if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):
          decrypted_output = decrypted_output + chr(char_position)
          continue
       char_position = char_position - 97
       new_char_position = char_position - key
       # works the same as 97 and modulu 26
       new_char_position = new_char_position % 26
       new_char_position = new_char_position + 97
       new_char = chr(new_char_position)
       if flag == 1:
          new_char = new_char.upper()
          flag = 0
       decrypted_output = decrypted_output + new_char

#    print("###################")
#    print("### Decrypted text:", decrypted_output)
#    print("###################")
    return decrypted_output


if __name__ == "__main__":
    main()




