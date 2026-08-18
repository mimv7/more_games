message = input()
new_message = ''
VOWELS = 'aeiouyеоаыяиэ'
for letter in message:
    print(letter)
    if letter.lower() not in VOWELS:
        new_message += letter

print(new_message)