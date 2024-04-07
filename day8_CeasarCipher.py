from utils import cipher_arts as ca

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(ca.logo)
finish = False
    
def ceaser(mode, text, shift_amount):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            if mode == "encode":
                position = alphabet.index(letter)
                new_position = position + shift_amount
            elif mode == "decode":
                position = alphabet.index(letter, 26)
                new_position = position - shift_amount
            new_text += alphabet[new_position]
        else:
            new_text += letter
    print(f"The {mode} result is: {new_text}")
    
while not finish:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))              
    ceaser(direction, text, shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if again == 'no':
        finish = True
    elif again == 'yes':
        pass
    else:
        break
            