def vowel(ch):
    vw=['a','A','e','E','i','I','o','O','u','U']
    if ch in vw:
        return True
    return False

ch=input()
if(vowel(ch)):
    print("Vowels")
else:
    print("is not Vowels")