# Palindrome Checker
import string

text = input("Enter text: ")

# Remove spaces, punctuation and convert to lowercase
cleaned_text = ""

for char in text:
    if char.isalnum():
        cleaned_text += char.lower()

if cleaned_text == cleaned_text[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")