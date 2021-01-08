import random
import subprocess

def main():
    username_password_generator()

def username_generator(first_name, last_name):
    if len(first_name) < 3:
      username = first_name
    else:
      username = first_name[:3]
    if len(last_name) < 4:
      username += last_name
    else:
      username += last_name[:4]    

    return username

def password_generator(username,length):
    password = ""
    symbols1 = "!@#)?/"
    symbols2 = "$=%^&*("
    num = random.randint(1,100000)
    temp = str(num) + symbols1 + username + symbols2

    for i in range(len(username)):
      temp += username[i-5]

    for i in range(length):
      password += random.choice(temp)

    return password

def username_password_generator():
    result = subprocess.Popen('zenity --forms --title="Username & Password Generator" \
                              --add-entry="First Name" \
                              --add-entry="Last Name" \
                              --add-entry="Password Length [12-16]"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

    #output = result.communicate()
    output = result.stdout.readline()
    #output = str(output[0]).strip()
    output =output.strip()
    output = output.split('|')
    first_name = output[0]
    last_name = output[1]
    length = int(output[2])
    #first_name = input("Enter your last name: ")
    #last_name = input("Enter your last name: ")
    flag = 0 

    """
   
     while True:
      length = int(input("Enter length of password [12-16]: "))
      if length >= 12:
       break
      else:
       print("Error, password length can't be less than [12]")
    
    """
    username = username_generator(first_name,last_name)
    password = password_generator(username,length)   
    print("Username:", username)
    print("Password:", password)

if __name__ == "__main__":
   main()

