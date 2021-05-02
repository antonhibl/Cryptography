# Made by Anton Hibl
# Made on April 30, 2021

# This program will simulate the 'Spoonerize' word-game between 2 words.
# Functions and such below here:

# List of all consonants in the English language
consonant_list = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "s",
    "t",
    "v",
    "x",
    "z",
    "h",
    "r",
    "w",
    "y",
]

# This function takes an input from the user
def take_input():
    return input("Enter a word: ")


# This function determines if the 1st word starts with a consonant
# Return of 1 means only the 1st letter is, 2 means 2, etc
def determine_word_start(str):
    if str[0] in consonant_list:
        if str[1] in consonant_list:
            if str[2] in consonant_list:
                return 3
            else:
                return 2
        else:
            return 1
    else:
        return 0


# Returns a slice of the string based on the consonant function
def slicer(int, str):
    if int == 0:
        slicey = ""
    elif int == 1:
        slicey = str[0:1]
    elif int == 2:
        slicey = str[0:2]
    elif int == 3:
        slicey = str[0:3]
    return slicey


# Main goes below here
def main():
    input1 = take_input()
    input2 = take_input()
    # determine consonants at word start for each string
    wordstart1 = determine_word_start(input1)
    wordstart2 = determine_word_start(input2)
    # take slices of both original inputs
    slice1 = slicer(wordstart1, input1)
    slice2 = slicer(wordstart2, input2)
    # Creating new strings to add slices to
    newstr1 = input1[wordstart1:]
    newstr2 = input2[wordstart2:]
    # Add slices I took to the new strings
    finalstr1 = slice2 + newstr1
    finalstr2 = slice1 + newstr2
    # Print the final string
    print(f"{finalstr1} {finalstr2}")
    exit


# Main runs below here
main()
