import subprocess, sys

def main():

	answer = input("Do you want to [I]NSTALL, [U]NINSTALL, or [T]ry the program?(I/u/T): ")
	install_uninstall_try(answer)


def install_uninstall_try(answer):
	try:
		line_removal = 'echo -ne "\033[A\033[2K\r"'
		if answer == 'I' or answer == 'i':
			check_installation = 'echo -ne "\033[A\033[2K\r";find /usr/bin/ -name "cipher_utility" | grep -o cipher_utility >/dev/null 2>&1'
			call1 = subprocess.call(check_installation, shell=True)
			if call1 == 0:
				print("Program is already installed!")
				sys.exit(0)
			else:
				install = 'echo -ne "\033[A\033[2K\r";chmod +x cipher_utility;sudo cp cipher_utility /usr/bin/;chmod -x cipher_utility;mkdir cipher-utility; cp -r $(ls -A | grep -v "cipher-utility") cipher-utility/;mv cipher-utility ~/;cd ~/cipher-utility &&\
				echo -e "[Desktop Entry]\nName=Cipher Utility\nStartupWMClass=Cipher Utility\nComment=Encryption/Decryption Utility\nExec=/usr/bin/cipher_utility\nType=Application\nCategories=Utility" > cipher_utility.desktop;\
				path=$PWD;if !([[ $(grep -o "Icon" cipher_utility.desktop) == "Icon" ]]);then echo "Icon=$path/icon.png" >> cipher_utility.desktop;fi;sudo cp cipher_utility.desktop /usr/share/applications/;rm cipher_utility.desktop'
				call2 = subprocess.call(install, shell=True)

		elif answer == 'U' or answer == 'u':
			uninstall = 'echo -ne "\033[A\033[2K\r";sleep 1;sudo rm /usr/bin/cipher_utility >/dev/null 2>&1 && sudo rm /usr/share/applications/cipher_utility.desktop >/dev/null 2>&1 && rm -rf ~/cipher-utility >/dev/null 2>&1'
			call2 = subprocess.call(uninstall, shell=True)
		elif answer == 'T' or answer == 't':
			call2 = subprocess.call(line_removal, shell=True)
			program_try = 'python cipher_utility.py'
			call3 = subprocess.call(program_try, shell=True)
			sys.exit(0)
		else:
			call2 = subprocess.call(line_removal, shell=True)
			print("#############################")
			print("### Error, Entry missing! ###")
			print("#############################")
			sys.exit(1)

		print("##################")
		print("### Successful ###")
		print("##################")
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()