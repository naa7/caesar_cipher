import subprocess, sys

def main():

	answer = input("Do you want to [I]NSTALL or [U]NINSTALL the program?(I/u): ")
	if answer == 'I' or answer == 'i':
		install_1 = 'echo -ne "\033[A\033[2K\r";sleep 1;sudo cp cipher_utility /usr/bin/'
		install_2 = 'echo -e "[Desktop Entry]\nName=Cipher Utility\nStartupWMClass=Cipher Utility\nComment=Encryption/Decryption Utility\nExec=/usr/bin/cipher_utility\nType=Application\nCategories=Utility;\n" > cipher_utility.desktop'
		install_3 = 'path=$PWD;if !([[ $(grep -o "Icon" cipher_utility.desktop) == "Icon" ]]);then echo "Icon=$path/icon.png" >> cipher_utility.desktop;fi;sudo cp cipher_utility.desktop /usr/share/applications/;rm cipher_utility.desktop'	
		call_1 = subprocess.call(install_1, shell=True)
		call_2 = subprocess.call(install_2, shell=True)
		call_3 = subprocess.call(install_3, shell=True)
	elif answer == 'U' or answer == 'u':
		uninstall = 'echo -ne "\033[A\033[2K\r";sleep 1;sudo rm /usr/bin/cipher_utility >/dev/null 2>&1 && sudo rm /usr/share/applications/cipher_utility.desktop >/dev/null 2>&1'
		call = subprocess.call(uninstall, shell=True)
	else:
		line_removal = 'echo -ne "\033[A\033[2K\r"'
		call = subprocess.call(line_removal, shell=True)
		print("#############################")
		print("### Error, Entry missing! ###")
		print("#############################")
		sys.exit(1)

	print("##################")
	print("### Successful ###")
	print("##################")

if __name__ == "__main__":
	main()