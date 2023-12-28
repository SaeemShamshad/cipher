message = input("enter your message to be ciphered:")
for x in message :
    if x != " ":
        unicode = ord(x)
        n_factor = unicode - 97
        new_unicode = unicode + (25 - n_factor*2)
        print(chr(new_unicode))    
    elif x == " ":
        print(" ")
