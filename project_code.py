# -*- coding: utf-8 -*-
"""Project_code.ipynb

Automatically generated by Colaboratory.

SECURE COMUNICATION SYSTEM

CRYPTOGRAPHY SYSTEM USING VIGENERE CIPHER AND POLYBIUS CIPHER

By- SHIVAM VATSHAYAN
"""

# Python code to implement 
# Vigenere Cipher 

# This function generates the  key in a cyclic manner until it's length isn't equal to the length of original text 



def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))

"""For Full Project Code, Mail me at vatshayan007@gmail.com Now.

Project is very Interesting and Easy to Understand

I will send you PPT, Report and Project code directly.

Mail me Now **vatshayan007@gmail.com** for Full Project !

Let's Learn, work and Grow together.
Ask freely!
"""



