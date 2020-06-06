# import pyfiglet module
import pyfiglet
#Text in slant font
out = pyfiglet.figlet_format("Caesar Cipher Algorithm")
print(out)
print("1. Plain Text -> Cipher Text")
print("2. Cipher Text -> Plain Text (without KEY)")
print("3. Cipher Text -> Plain Text (with KEY)")
dataset = 'abcdefghijklmnopqrstuvwxyz'
val = int(input())

if (val == 1):
    def encrypt(text,s):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    text = input('Plain Text : ')
    shift = int(input('Shift : '))
    print ("Cipher Text : " + encrypt(text,shift))

if(val == 2):
    def decrypt(text):
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in text:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            print("Plain Text with key #%s:%s" %(key,translated))


    text = input('Cipher Text : ')
    print('Trying all possible combinations.....')
    decrypt(text)

if(val == 3):
    def decrypt_withkey(text,s):
        result = ''
        for l in text:
            try:
                i = (dataset.index(l) - s) % 26
                result += dataset[i]
            except ValueError:
                result += l

        return result
    
    text = input('Cipher Text : ')
    s = int(input('Shift : '))
    print("Plain Text: " + decrypt_withkey(text,s))

    


   









