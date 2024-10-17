# Setting plaintext, shift values and result list
plaintext = input("Message:")
shift = int(input("Shift Value:"))
result = []

for char in plaintext:
    if char.isalpha():
        if char.isupper(): #ASCII range has diffrent values for upper and lower case values
            uppershift = ((ord(char) - 65 + shift) % 26) + 65 #Uppercase range starts at 65, and 26 letter in alphabet, so it loops around
            letter = chr(uppershift)
            result.append(letter)
        else:
            lowershift = ((ord(char) - 97 + shift) %26) + 97 #Lowercase range starts at 97
            letter = chr(lowershift)
            result.append(letter)
    else:
        result.append(char) # If char not alphabetic keep same value

encrypted_messaged = ''.join(result)
print(encrypted_messaged)
