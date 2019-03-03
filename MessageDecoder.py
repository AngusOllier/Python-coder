alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3

def transform_message(message, action):
  newMessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      if action == 'decode':
          new_position = (position - key) % 52
      else:
          new_position = (position + key) % 52
      new_character = alphabet[new_position]
      print('The new character is: ',new_character)
      newMessage += new_character
    else:
      newMessage += character
  return newMessage

message = input('Please enter your code: ')

decoded_message = transform_message(message, 'decode')
print(decoded_message)
