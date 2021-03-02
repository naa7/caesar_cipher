import subprocess, random

def main():
	cipher_utility()


def cipher_utility():
	try:
		input = subprocess.Popen('zenity --forms --title="Cipher Utility" --text="" --add-combo="Cipher type"\
			--combo-values="Caesar Cipher|ROT Cipher|Vigenere Cipher|Monoalphabetic Cipher|Gronsfeld Cipher|Tritheme Cipher"\
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

		if cipher == "Caesar Cipher" and text != "" and key != "":
			output1 = caesar_cipher(mode,text,int(key))
		elif cipher == "ROT Cipher" and text != "" and key != "":
			output1 = rot_cipher(mode,text,int(key),option)
		elif cipher == "Vigenere Cipher" and text != "" and key != "":
			output1 = vigenere_cipher(mode,text,key,option)
		elif cipher == "Monoalphabetic Cipher" and text != "":
			dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			if mode == 'Encrypt':
				key = get_random_key(dictionary)
				output1 = monoalphabetic_cipher(mode,text,key,dictionary,option)
				output1 = "Encrypted text: " + output1 + "\nKey: " + key
			else:
				if not(key_validity(key,dictionary)):
					print("Error found in key")
					exit(1)
				output1 = monoalphabetic_cipher(mode,text,key,dictionary,option)
		elif cipher == "Gronsfeld Cipher" and text != "":
			output1 = gronsfeld_cipher(mode,text,key,option)
		elif cipher == "Tritheme Cipher" and text != "":
			output1 = tritheme_cipher(mode,text,option)

		else:
			print("#############################")
			print("### Error, Entry missing! ###")
			print("#############################")
			exit(1)
        
		file = open("temp.txt", "w+")
		file.write(output1)
		file.close()
        
		if mode == 'Encrypt':
			output2 = 'cat temp.txt | zenity --width=400 --height=150 --title="Encrypted Text" --text-info && rm temp.txt'
		else:
			output2 = 'cat temp.txt | zenity --width=400 --height=150 --title="decrypted Text" --text-info && rm temp.txt'

		call = subprocess.call(output2, shell=True)

	except Exception as e:
		#print(e)
		print("############################")
		print("### Error, Program Exit! ###")
		print("############################")


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


def vigenere_cipher(mode,text,key,option):
	output = ""
	keyIndex = 0
	key = key.upper()
    
	for i in range(len(text)):
		text_letter = text[i]
		key_letter = key[keyIndex]
        
		if text_letter.islower() == True:
			text_letter = text_letter.upper()
        
		char_position = ord(text_letter)
		key_position = ord(key_letter)

		if not((char_position >= 65 and char_position <= 90) or (char_position >= 97 and char_position <= 122)):
			if option == 'Remove' and mode == 'Encrypt' and char_position == 32:
				continue	
			else:		
				output = output + chr(char_position)
				continue

		char_position = char_position - 65
        
		if mode == 'Encrypt':
			new_char_position = char_position + key_position
		elif mode == 'Decrypt':
			new_char_position = char_position - key_position

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


if __name__ == "__main__":
	main()


