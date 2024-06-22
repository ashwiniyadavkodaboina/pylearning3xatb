string = input("enter the string:")
vowels = "aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyz"
count = sum(string.count(vowel) for vowel in vowels)
print(f'count of vowels :{count}')
count1= sum(string.count(consonant) for consonant in consonants)
print(f'count of consonants:{count1}')


