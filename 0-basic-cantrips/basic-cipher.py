import sys


def caesar_cipher(text, shift):
    result = ""
    for char in text:           ## loop through everything
        if char.isalpha():      ## check if this is an actual word
            if char.islower():  ## If lower case
                ### (ord(char) - ord('a') ---> this gets the numerical place of the character input, and subtracts that from the first letter (lower case a)
                shifted_char = chr( (ord(char) - ord('a')  + shift) % 26 + ord('a'))
                ### add "shift" which is a character the user chooses
                ### modulus this amount by 26
                ### 1. Get the numerical placement of the original character, subtract this from a's number, and add the shift variable we specified
                ### 2. Divide this by 26 and then add the # of a 
            else:
                shifted_char = chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char
    
    return result





def main():
    while(True):
        originaltext = input("String to cipher:\n")
        shift = input("How Many Spaces:\n")
       ## handstitched(originaltext, shift)
 
if __name__ == "__main__":
    main()

