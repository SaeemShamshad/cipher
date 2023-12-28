message = input("enter your message to be ciphered:")
 
for x in message :
    unicode = ord(x)
    n_factor = unicode - 97
    new_unicode = unicode + (25 - n_factor*2)
    print(chr(new_unicode))    
