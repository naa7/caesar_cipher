def morse_cipher(mode,text,option):
	morse_dictionary = {
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
				if text[i].lower() in morse_dictionary:
					output = output + morse_dictionary[text[i].lower()] + " "
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
			for key, value in morse_dictionary.items():
				if element == value:
					output = output + key
					break
				elif element == '':
					output = output + ' '
					break
				else:
					continue
			
	return output



text1 = "Hi There! how are you?"
text2 = ".... .. - .... . .-. . -.-.-- .... --- .-- .- .-. . -.-- --- ..- ..--.."
mode1 = "Encrypt"
mode2 = "Decrypt"
option = "Remove"
print(morse_cipher(mode1,text1,option))
print(morse_cipher(mode2,text2,option))