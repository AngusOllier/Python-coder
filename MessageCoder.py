alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3

def encode( message ):
  newMessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      new_position = (position + key) % 52
      new_character = alphabet[new_position]
      print('The new character is: ',new_character)
      newMessage += new_character
    else:
      newMessage += character
  return newMessage

message = input('Please enter a message: ')

new_message = encode(message)

print(new_message)

