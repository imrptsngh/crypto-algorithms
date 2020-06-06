
print("********* ROT13 Implemetation *********")
print("1. Plain Text -> Cipher Text")
print("2. Cipher Text -> Plain Text")
val = int(input())

if(val == 1):
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

    def rot13(text):
        return text.translate(rot13trans)

    txt = input('Plain Text : ')
    print ("Cipher Text : " + rot13(txt))

if(val == 2):
    rot13trans = str.maketrans('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

    def rot13_rev(text):
        return text.translate(rot13trans)

    txt = input('Cipher Text : ')
    print ("Plain Text : " + rot13_rev(txt))
