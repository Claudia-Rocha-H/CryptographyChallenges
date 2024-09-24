text = "This is my secret message."
letters = "abcdefghijklmnopqrstuvwxyz"
key = 4
textencrypt = "EQFMHIBXVSYW: EFPI XS TMGO AMXL IUYEP WOMPP E VMKLX-LERH TSGOIX SV E PIJX"
keyencrypt = 13
def encrypt(text, key, letters):
    text = text.lower()
    newString = ""
    ind = 0
    for i in text:
        if i in letters:
            ind = letters.index(i) + key
            if ind >= 26:
                ind = ind - 26
        
            newString += letters[ind]  
        else:
            newString += i
    print("-------------------------------------------------------------------------------------------------")
    print("Encrypted string: "+newString.upper())
    print("-------------------------------------------------------------------------------------------------")

encrypt(text, key, letters)

def decrypt(textencrypt, keyencrypt, letters):
    textencrypt = textencrypt.lower()
    newString = ""
    ind = 0
    for i in textencrypt:
        if i in letters:
            ind = letters.index(i) - keyencrypt
            if ind < 0:
                ind = ind + 26
        
            newString += letters[ind]  
        else:
            newString += i
    print("-------------------------------------------------------------------------------------------------")
    print("Decrypted string: "+newString.upper())
    print("-------------------------------------------------------------------------------------------------")
    print("")

decrypt(textencrypt, key, letters)