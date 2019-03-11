from flask import Flask, render_template, request

application = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

@application.route('/', methods=['GET'])
def codec():
    return render_template('decoder.html')


@application.route('/', methods=['POST'])
def do_codec():
    action = request.form['action']
    transformed = transform(request.form['message'], action)
    return render_template('decoder.html', action=action, transformed=transformed)


def transform(message, action, key=3):
    newMessage = ''
    for character in message:
        position = alphabet.find(character)
        if position >= 0:
            if 'encrypt' == action:
                new_position = (position + key) % 52
            else:
                new_position = (position - key) % 52
            new_character = alphabet[new_position]
            newMessage += new_character
        else:
            newMessage += character
    return newMessage


if __name__ == "__main__":
    application.run()
