# Setting plaintext vales and result list
result = []
plaintext = input("Message:")

# Input validation
while True:
    subkey = input("Key:")
    if len(subkey) != 26 or not subkey.isalpha() or not subkey.isupper(): #Requires key that is same size as alphabet, only allowing alphabet chars, and uppercased to avoid more ASCII computation.
        print("Wrong Input. Key must be 26 characters long, all Upper-Cased and only alphabetic.")
        continue
    else:
        break

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sub_dict = {alphabet[i]: subkey[i] for i in range(26)} #Setting pairs with key and alphabet

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            result.append(sub_dict[char]) #If char is alphabetic substitute
        else:
            result.append(sub_dict[char.upper()].lower()) #If not keep same value
    else:
        result.append(char)


encrypted_message = ''.join(result) 
print(encrypted_message)