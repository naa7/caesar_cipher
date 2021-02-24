# caesar_cipher project

![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103) <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"> <img src="https://img.shields.io/github/stars/naa-7/caesar_cipher?style=social"> <img src="https://img.shields.io/github/repo-size/naa-7/caesar_cipher"> [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/naa-7/caesar_cipher/LICENSE)

![img_1](https://github.com/naa7/caesar_cipher/blob/main/images/caesar_encrypt1.png) 
![img_2](https://github.com/naa7/caesar_cipher/blob/main/images/caesar_encrypt2.png) 
![img_3](https://github.com/naa7/caesar_cipher/blob/main/images/caesar_decrypt1.png) 
![img_4](https://github.com/naa7/caesar_cipher/blob/main/images/caesar_decrypt2.png)
![img_5](https://github.com/naa7/caesar_cipher/blob/main/images/rot_encrypt1.png)
![img_6](https://github.com/naa7/caesar_cipher/blob/main/images/rot_encrypt2.png)
![img_7](https://github.com/naa7/caesar_cipher/blob/main/images/rot_decrypt1.png)
![img_8](https://github.com/naa7/caesar_cipher/blob/main/images/rot_decrypt2.png) 


The idea of this project is to encrypt and decrypt data using caesar cipher. The way caesar cipher works is by 

shifting a character three positions forward when encrypting and three positions backward when decrypting, in

the ASCII table. For example xample, to encrypt `I am here`, we need to shift each letter specific positions

forward. For example, Each letter will shift 3 positions. (1)`J` --> (2)`K` --> (3)`L`, so `I` will become

`L`. The white space `" "` will become `#`, `a` --> `d`, `m` --> `p` and so on. Therefore, our encrypted 

text will be `L#dp#khuh`. To decrypt it, we will do the opposite. Instead of moving three positions 

forward, we will move three positions backward, `L` --> `I`, `#` --> `" "`, `d` --> `a` and so on.


### To run the program:

    $ python caesar_cipher.py
