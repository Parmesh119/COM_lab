def vowel(ch):
    vw=['a','A','e','E','i','I','o','O','u','U']
    if ch in vw:
        return True
    return False

ch=input()
if(vowel(ch)):
    print(ch+" is a Vowels")
else:
    print(ch+" is not a Vowels")