def answer(s):
    # your code here
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    decoded_s = ""

    # Go through every letter in s
    # See if it is in the alphabet list
    # If so, take out that position, and apply it in reverse
        # For 'b', is in position 1, take out position -2
    # Replace that letter with the current letter, and move to the next letter
    # Repeat till EOF


    for letter in s:
        if (letter in alphabet):
            opp_letter = alphabet.index(letter)
            decoded_s += alphabet[-opp_letter-1]
        else:
            decoded_s += letter

    return decoded_s

print(answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
