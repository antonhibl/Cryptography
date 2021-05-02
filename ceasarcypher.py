# gh0u1
# made on April 29, 2021

""" 
This program will be able to encrypt messages into a 
Ceasar Cypher which can be modified for a shift between 
1 and 25 characters. Vice Versa this will be able to decrypt
any message and set for any value as a key for shifting 
between 1 and 25 characters. 
"""
import string

# Defines a dictionary of the alphabet
alphabet_string = string.ascii_lowercase
abcs = list(alphabet_string)

# Function to choose between encryption or decryption
def encrypt_or_decrypt():
    choiceED = input("Would You like to ENCRYPT or DECRYPT?\n")
    choiceED = choiceED.upper()
    if choiceED == "ENCRYPT":
        return 1
    elif choiceED == "DECRYPT":
        return 2
    else:
        exit


# Function to determine a shift value between 1 and 25
def determine_shift():
    shiftval = int(input("Input a Shift Value(between -25 and -1 or 1 and 25):\n"))
    if shiftval <= -1 and shiftval >= -25:
        return shiftval
    elif shiftval >= 1 and shiftval <= 25:
        return shiftval
    else:
        exit


# Function to solicit a string of text from the user
def solicit_text():
    text = input("Input text here:\n")
    return text


# Function to Encrypt a string
def encrypt(plaintext, shift):
    encryption = ""
    for c in plaintext.upper():
        # check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            # perform the shift
            new_index = (c_index + shift) % 26
            # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            # append to encrypted string
            encryption = encryption + new_character
        # Removes Spaces
        elif c == " ":
            pass
        else:
            # since character is not uppercase, leave it as it is
            encryption += c
    return encryption


def decrypt(cyphertext, key):
    plain_text = ""
    for c in cyphertext.upper():
        # check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            # perform the negative shift
            new_index = (c_index - key) % 26
            # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            # append to plain string
            plain_text = plain_text + new_character
        else:
            # since character is not uppercase, leave it as it is
            plain_text += c
    return plain_text


# Main is below:
def main():
    startchoice = encrypt_or_decrypt()

    # This path leads to Encryption
    if startchoice == 1:
        plaintext = solicit_text()
        shift = determine_shift()
        cyphertext = encrypt(plaintext, shift)
        print(f"Here is your encrypted message:\n'{cyphertext}'")

    # This path leads to Decryption
    elif startchoice == 2:
        cyphertext = solicit_text()
        key = determine_shift()
        plaintext = decrypt(cyphertext, key)
        print(f"Here is your decrypted message:\n'{plaintext}'")

    # This exits all of Main
    exit


# Calls the program
main()
