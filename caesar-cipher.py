# import pyfiglet module
import pyfiglet
#Text in slant font
out = pyfiglet.figlet_format("Caesar Cipher Algorithm")
print(out)
print("1. Plain Text -> Cipher Text")
print("2. Cipher Text -> Plain Text")
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

   









