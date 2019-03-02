alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3
newMessage = ''

message = input('Please enter a message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 52
    newCharacter = alphabet[newPosition]
    print('The new character is: ',newCharacter)
    newMessage += newCharacter
  else:
    newMessage += character
print(newMessage)
