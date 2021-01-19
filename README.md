# caesar_cipher project

![img_1](https://github.com/naa-7/caesar_cipher/blob/main/img_1.png)
![img_2](https://github.com/naa-7/caesar_cipher/blob/main/img_2.png)
![img_3](https://github.com/naa-7/caesar_cipher/blob/main/img_3.png)
![img_4](https://github.com/naa-7/caesar_cipher/blob/main/img_4.png) 



The idea of this project is to encrypt and decrypt data using caesar cipher. The way caesar cipher works is by 

shifting a character three positions forward when encrypting and three positions backward when decrypting, in

the ASCII table. For example xample, to encrypt `I am here", we need to change each character to third 

character that comes after it. (1)`J` --> (2)`K` --> (3)`L`, so `I` will become `L`. The white space `" "`

will become `#`, `a` --> `d`, `m` --> `p` and so on. Therefore, our encrypted text will be `L#dp#khuh`.

To decrypt it, we will do the opposite. Instead of moving three positions forward, we will move three

positions backward, `L` --> `I`, `#` --> ` `, `d` --> `a` and so on.


### To run the program:

    $ python caesar_cipher.py
