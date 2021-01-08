# username_password_generator

The idea of this project is to generate a username using the first three letters of user's firstname and the first four letters of user's lastname.

Also, to generate a password of a length set by user. The password is produced by combining random numbers, symbols, and username and
 
then randomly choosing from the list to come up with a password. Zenity is used by the program prompting the user to input their firstname,

lastname, and length of password which is then directed to the python program. Finally, optional, the username, and password are directed to

zenity for displaying through a simple bash script.


## There are two ways to run the program

 One, username & password output will be displayed in the terminal:

    $ python username_password_generator.py


Second, username & password output will be displayed on Zenity:
   
    $ chmod +x python_to_zenity.sh

    $ ./python_to_zenity.sh
