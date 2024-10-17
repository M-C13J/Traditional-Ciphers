
result = []
plaintext = input("Enter Message:")

# Key validation
while True:
    vigkey = input("Key: ")
    if not vigkey.isalpha():
        print("Wrong Input, please only use alphabetic characters.")
        continue
    else:
        # Extend the key to match the length of the plaintext
        if len(vigkey) != len(plaintext):
            extended_key = (vigkey * (len(plaintext) // len(vigkey))) + vigkey[:len(plaintext) % len(vigkey)]
            vigkey = extended_key
        break

# Encrypt each character of plaintext
for i in range(len(plaintext)):
    char = plaintext[i]
    vig_char = vigkey[i]

    if char.isalpha():
        if char.isupper():
            shift = ((ord(char) - 65) + (ord(vig_char.upper()) - 65)) % 26 #Uppercase range starts at 65
            letter = chr(shift + 65)  # 
            result.append(letter)
        else:
            shift = ((ord(char) - 97) + (ord(vig_char.lower()) - 97)) % 26 #Lowercase range starts at 65
            letter = chr(shift + 97)
            result.append(letter)
    else:
        result.append(char)  # Keep non-alphabet characters unchanged


encrypted_message = ''.join(result)
print("Encrypted Message:", encrypted_message)

