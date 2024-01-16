def isvowel(str):
        if len(str) > 1:
            return False
        elif str in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False

def nov(str):

    vowel_count = 0

    for letter in str:
        if isvowel(letter) == True:
            vowel_count += 1
    
    return vowel_count