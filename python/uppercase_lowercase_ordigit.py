# character uppercase lowercase digit check

character = input("type a !SINGLE! CHARACTER: \t")

if(ord(character) >= ord("a") and ord(character) <= ord("z")):
    print("Lowercase")

elif(ord(character) >= ord("A") and ord(character) <= ord("Z")):
    print("Uppercase")

    
elif(ord(character) >= ord("0") and ord(character) <= ord("9")):
    print("digit")
    
else:
    print("Other")
