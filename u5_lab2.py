# Basic definition of vowels and consonants as either a str or list value, subject to change 

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
name = "John Doe"
vowel_count = 0
consonant_count = 0


for letter in name:
    if letter in vowels:
        vowel_count += 1

for letter in name:
    if letter in consonants:
        consonant_count += 1


print(vowel_count)
print(consonant_count)