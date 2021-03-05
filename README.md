# cipher_utility project

![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103) <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"> <img src="https://img.shields.io/github/stars/naa-7/caesar_cipher?style=social"> <img src="https://img.shields.io/github/repo-size/naa-7/caesar_cipher"> [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/naa-7/caesar_cipher/LICENSE)

<img src="https://github.com/naa7/cipher_utility/blob/main/images/manual.png" width=400>
<img src="https://github.com/naa7/cipher_utility/blob/main/images/cipher_utility.png" width=350></br> 


The idea of this project is to encrypt and decrypt data using different cipher types.For examples, The way caesar 
cipher works is by shifting a character `x` positions forward when encrypting and `x` positions backward when 
decrypting, in the ASCII table. For example xample, to encrypt `I am here`, we need to shift each letter specific
positions forward. For example, Each letter will shift 3 positions. (1)`J` --> (2)`K` --> (3)`L`, so `I` will
become `L`. The white space `" "` will become `#`, `a` --> `d`, `m` --> `p` and so on. Therefore, our encrypted 
text will be `L#dp#khuh`. To decrypt it, we will do the opposite. Instead of moving three positions 
forward, we will move three positions backward, `L` --> `I`, `#` --> `" "`, `d` --> `a` and so on.


## To run the program:

    $ cd && git clone https://github.com/naa7/cipher_utility.git

    $ cd cipher_utility/exec_files/ && ./cipher_utility

    $ cd cipher_utility/python_files/ && python cipher_utility.py

## Optional

For easier use of the timer without the need to navigate to its directory and run the file,

run `installer_uninstaller` for installing and uninstalling:
    
    $ cd cipher_utility/exec_files/ && ./installer_uninstaller

Now, you can either open it from terminal

    $ cipher_utility

Or, open it from applications menu
