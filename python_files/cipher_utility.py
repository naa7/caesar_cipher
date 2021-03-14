import subprocess, random, sys

def main():
	cipher_utility()


def cipher_utility():
	
	install = 'if ! (dpkg -s zenity >/dev/null 2>&1) && ! (rpm -q zenity >/dev/null 2>&1) && ! (yum list installed zenity >/dev/null 2>&1) && ! (dnf list installed zenity >/dev/null 2>&1)\
			&& ! (which zenity >/dev/null 2>&1 && echo $? >/dev/null 2>&1);then echo -n "Zenity is required to run the program, Do you want to install it?(Y/n): ";read answer;\
			echo -ne "\033[A\033[2K\r";if [[ $answer == "Y" || $answer == "y" ]];then if ! (sudo apt-get -y install zenity >/dev/null 2>&1) && ! (yes | sudo pacman -S zenity >/dev/null 2>&1)\
			&& ! (sudo yum -y install zenity >/dev/null 2>&1);then echo "Package Couldn\'t be installed. You need to install it manually!";else echo -ne "\033[A\033[2K\r";fi;else \
			echo "You need to install zenity";echo "Program Exit!";exit 1;fi;fi;'

	if (subprocess.call(install, shell=True)) == 1:
		sys.exit(1)

	file = open("manpage.txt","w+")
	file.write('<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body style="background-color:black;color:LightGray;">\n<h2 style="text-align:center;"><u>Manual</u></h2>\n<p>\n<b style="font-size:14px;"><u>Cipher types:</u></b>\n\
	<ul style="font-size:13px;margin-bottom: 20px;">\n<li style="margin-top: -5px;">Caesar Cipher</li>\n<li>ROT Cipher</li>\n<li>Vigenere Cipher</li>\n<li>Monoalphabetic Cipher</li>\n<li>Gronsfeld Cipher</li>\n\
	<li>Tritheme Cipher</li>\n<li>A1Z26 Cipher</li>\n<li>Morse Code Cipher</li>\n</ul>\n<b style="font-size:14px;"><u>Modes:</u></b>\n<ul style="font-size:13px;margin-bottom: 20px;">\n<li style="margin-top: -5px;">Encryption</li>\n<li>Decryption</li>\n</ul>\n\n\
	<b style="font-size:14px;"><u>Word boundaries:</u></b>\n<ul style="font-size:13px;margin-bottom: 20px;">\n<li style="margin-top: -5px;">This <b>ONLY</b> works for encryption</li>\n</ul>\n\n\
	<b style="font-size:14px;"><u>Cipher key:</u></b>\n<ul style="font-size:13px;margin-bottom: 20px;">\n<li style="margin-bottom: 7px;margin-top: -5px">Caesar cipher\
	accepts a <b>NUMBER</b> key for both encryption and decryption</li>\n<li style="margin-bottom: 7px;">ROT cipher accepts a <b>NUMBER</b> key for both encryption and decryption</li>\n\
	<li style="margin-bottom: 7px;">Vigenere cipher accepts a <b>LETTER</b> key for both encryption and decryption</li>\n<li style="margin-bottom: 7px;">Monoalphabetic cipher accepts\
	<b>ONLY</b> a key for decryption</li>\n<li style="margin-bottom: 7px;">Gronsfeld Cipher accepts a <b>NUMBER</b> key for both encryption and decryption</li>\n<li style="margin-bottom: 7px;">Tritheme cipher\
	does <b>NOT</b> accept a key for encryption or decryption</li>\n<li style="margin-bottom: 7px;">A1Z26 cipher does <b>NOT</b> accept a key for encryption or decryption</li>\n<li style="margin-bottom: 7px;">Morse Code cipher\
	does <b>NOT</b> accept a key for encryption or decryption</li>\n</ul>\n\n<b style="font-size:14px;"><u>Enter text:</u></b>\n<ul style="font-size:13px;">\n\
	<li style="margin-top: -5px;">Here, you enter the text to be either encrypted or decrypted</li>\n</ul>\n</p>\n</body>\n</html>')
	file.close()

	manual_removal = 'rm manpage.txt'
	manual = 'zenity --title="Cipher Utility" --text-info --height=650 --width=530 --html --filename=manpage.txt --ok-label="NEXT" --cancel-label="EXIT" 2>/dev/null'

	if (subprocess.call(manual, shell=True)) == 1:
		print("#####################")
		print("### Program Exit! ###")
		print("#####################")
		subprocess.call(manual_removal, shell=True);
		sys.exit(1)
	else:
		subprocess.call(manual_removal, shell=True);
		while True:
			try:
				input = subprocess.Popen('zenity --forms --title="Cipher Utility" --text="" --ok-label="Next" --cancel-label="Exit" --add-combo="Cipher type"\
					--combo-values="Caesar Cipher|ROT Cipher|Vigenere Cipher|Monoalphabetic Cipher|Gronsfeld Cipher|Tritheme Cipher|A1Z26 Cipher|Morse Code Cipher"\
					--add-combo="Mode" --combo-values="Encrypt|Decrypt"\
					--add-combo="Word boundaries" --combo-values="Keep|Remove" --add-entry="Cipher key"\
					--add-entry="Enter text"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
			
				input = input.stdout.readline()
				input = input.strip()
				ind = index_list(input,'|')
				cipher = input[:ind[0]]
				mode = input[ind[0]+1:ind[1]]
				option = input[ind[1]+1:ind[2]]
				key = input[ind[2]+1:ind[3]]
				text = input[ind[3]+1:]
				dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

				if cipher == "Caesar Cipher" and text != "" and key != "":
					output1 = caesar_cipher(mode,text,int(key))
				elif cipher == "ROT Cipher" and text != "" and key != "":
					output1 = rot_cipher(mode,text,int(key),option)
				elif cipher == "Vigenere Cipher" and text != "" and key != "":
					key = key.upper()
					output1 = vigenere_cipher(mode,text,key,dictionary,option)
				elif cipher == "Monoalphabetic Cipher" and text != "":
					if mode == 'Encrypt':
						key = get_random_key(dictionary)
						output1 = monoalphabetic_cipher(mode,text,key,dictionary,option)
						output1 = "Encrypted text: " + output1 + "\nKey: " + key
					else:
						key = key.upper()
						if not(key_validity(key,dictionary)):
							print("Error found in key")
							sys.exit(1)
						output1 = monoalphabetic_cipher(mode,text,key,dictionary,option)
				elif cipher == "Gronsfeld Cipher" and text != "":
					output1 = gronsfeld_cipher(mode,text,key,option)
				elif cipher == "Tritheme Cipher" and text != "":
					output1 = tritheme_cipher(mode,text,option)
				elif cipher == "A1Z26 Cipher" and text != "":
					output1 = a1z26_cipher(mode,text,dictionary,option)
				elif cipher == "Morse Code Cipher" and text != "":
					output1 = morse_code_cipher(mode,text,option)
				else:
					print("#############################")
					print("### Error, Entry missing! ###")
					print("#############################")
					sys.exit(1)
			
				file = open("temp.txt", "w+")
				file.write(output1)
				file.close()
			
				if mode == 'Encrypt':
					output2 = 'cat temp.txt | zenity --width=400 --height=150 --title="Encrypted Text" --text-info --ok-label="DONE" --cancel-label="BACK" && rm temp.txt'
				else:
					output2 = 'cat temp.txt | zenity --width=400 --height=150 --title="decrypted Text" --text-info --ok-label="DONE" --cancel-label="BACK" && rm temp.txt'

				call = subprocess.call(output2, shell=True)

			except Exception as e:
				#print(e)
				print("#####################")
				print("### Program Exit! ###")
				print("#####################")
				break;


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


def get_random_key(dictionary):
	key = list(dictionary)
	random.shuffle(key)
	return ''.join(key)


def key_validity(key,dictionary):
	keyList = list(key)
	dictionaryList = list(dictionary)
	keyList.sort()
	dictionaryList.sort()
	return keyList == dictionaryList


def caesar_cipher(mode,text,key):
	output = ""
    
	for i in range(len(text)):
		#Obtain the ASCII value using ord
		char_position = ord(text[i])
		char_position = char_position - 32
        
		if mode == 'Encrypt':
			new_char_position = char_position + key
		elif mode == 'Decrypt':
			new_char_position = char_position - key
        
		new_char_position = new_char_position % 94
		new_char_position = new_char_position + 32
		new_char = chr(new_char_position)
		output = output + new_char

	return output


def rot_cipher(mode,text,key,option):
	output = ""

	for i in range(len(text)):
		letter = text[i]
        
		if letter.isupper() == True:
			letter = letter.lower()
        
		char_position = ord(letter)
        
		if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):			
			if option == 'Remove' and mode == 'Encrypt' and char_position == 32:
				continue	
			else:		
				output = output + chr(char_position)
				continue

		char_position = char_position - 97
        
		if mode == 'Encrypt':
			new_char_position = char_position + key
		elif mode == 'Decrypt':
			new_char_position = char_position - key
        
		new_char_position = new_char_position % 26
		new_char_position = new_char_position + 97
		new_char = chr(new_char_position)
        
		if text[i].isupper():
			new_char = new_char.upper()

		output = output + new_char

	return output


def vigenere_cipher(mode,text,key,dictionary,option):
	output = ""
	letters = dictionary
	keyIndex = 0
    
	for i in range(len(text)):
		letter_index = letters.find(text[i].upper())

		if letter_index != -1:		
			if mode == 'Encrypt':
				letter_index = letter_index + letters.find(key[keyIndex])
			elif mode == 'Decrypter':
				letter_index = letter_index - letters.find(key[keyIndex])

			letter_index = letter_index % 26
			
			if text[i].isupper():
				output = output + letters[letter_index]
			elif text[i].islower():
				output = output + letters[letter_index].lower()

			keyIndex = keyIndex + 1

			if keyIndex == len(key):
				keyIndex = 0
		else:
			char_position = ord(text[i])

			if option == 'Remove' and mode == 'Encrypt' and char_position == 32:
				continue
			else:
				output = output + text[i]
				continue     

	return output

    
def monoalphabetic_cipher(mode,text,key,dictionary,option):
	output = ""
	letters = dictionary
	keys = key

	if mode == 'Decrypt':
		letters, keys = keys, letters

	for i in range(len(text)):
		if text[i].upper() in letters:
			index = letters.find(text[i].upper())
			if text[i].isupper():
				output = output + keys[index].upper()
			else:
				output = output + keys[index].lower()
		else:
			if (option == 'Keep') or (option == 'Remove' and mode == 'Decrypt'):
				output = output + text[i]
			else:
				continue
	return output


def gronsfeld_cipher(mode,text,key,option):
	output = ""
	keyIndex = 0
	
	for i in range(len(text)):
		text_letter = text[i]
		key_character = key[keyIndex]
		
		if text_letter.islower() == True:
			text_letter = text_letter.upper()

		char_position = ord(text_letter)
		
		if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):
			if option == 'Remove' and mode == 'Encrypt' and char_position == 32:
				continue	
			else:		
				output = output + chr(char_position)
				continue

		char_position = char_position - 65

		if mode == 'Encrypt':
			new_char_position = char_position + int(key[keyIndex])
		else:
			new_char_position = char_position - int(key[keyIndex])

		new_char_position = new_char_position % 26
		new_char_position = new_char_position + 65
		new_char = chr(new_char_position)
		keyIndex = keyIndex + 1

		if keyIndex == len(key):
			keyIndex = 0
		
		if text[i].islower():
			new_char = new_char.lower()

		output = output + new_char

	return output


def tritheme_cipher(mode,text,option):
	output = ""
	key = 0
	
	for i in range(len(text)):
		text_letter = text[i]
		
		if text_letter.islower() == True:
			text_letter = text_letter.upper()

		char_position = ord(text_letter)
		
		if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):
			if option == 'Remove' and mode == 'Encrypt' and char_position == 32:
				continue	
			else:		
				output = output + chr(char_position)
				continue

		char_position = char_position - 65

		if mode == 'Encrypt':
			new_char_position = char_position + key
		else:
			new_char_position = char_position - key

		new_char_position = new_char_position % 26
		new_char_position = new_char_position + 65
		new_char = chr(new_char_position)
		key = key + 1

		if key == 26:
			key = 0
		
		if text[i].islower():
			new_char = new_char.lower()

		output = output + new_char

	return output

def a1z26_cipher(mode,text,dictionary,option):
	output = ""
	letters = dictionary
	
	if mode == 'Encrypt':
		for i in range(len(text)):
			if text[i].upper() in letters:
				if i == len(text) - 1:
					output = output + str(letters.find(text[i].upper())+1)
				else:				
					output = output + str(letters.find(text[i].upper())+1) + "-"
			else:
				if ((option == 'Keep') or (option == 'Remove' and mode == 'Decrypt')) and (ord(text[i]) == 32 or ord(text[i]) == 46):		
					if output[-1] == '-':
						output = output[:-1]
					if ord(text[i]) == 46:
						output = output + ' |'
					else:
						output = output + text[i]
				else:
					if output[-1] == '-':
						output = output[:-1]
					continue
	else:
		index = text.split()
		for  i in index:
			elements = i.split('-')
			for j in elements:
				if j != '' and j != '|':
					output = output + letters[int(j)-1].lower()
				else:
					output = output + j
					continue
			output = output + " "
	return output


def morse_code_cipher(mode,text,option):
	morse_code_dictionary = {
        # Letters
	"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", 
	"n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        # Numbers
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        # Punctuation
        "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.", ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-", "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-.",
		}
	output = ""
	if mode == 'Encrypt':
		for i in range(len(text)):
				if text[i].lower() in morse_code_dictionary:
					output = output + morse_code_dictionary[text[i].lower()] + " "
				elif option == 'Keep' and ord(text[i]) == 32:
					output = output + text[i]
				else:
					continue
	else:
		elements = text.split(" ")
		for element in elements:
			
    			#Iterate keys of dict: keys()
    			#Iterate values of dict: values()
    			#Iterate key-value pairs of dict: items()
			for key, value in morse_code_dictionary.items():
				if element == value:
					output = output + key
					break
				elif element == '':
					output = output + ' '
					break
				else:
					continue
			
	return output



if __name__ == "__main__":
	main()


