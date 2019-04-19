from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?'

@application.route('/', methods=['GET'])
def show_form():
    message = request.args.get('message', '')
    encrypted = request.args.get('encrypted', '')
    return render_template('decoder.html', message=message, encrypted=encrypted)


@application.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    transformed = transform(message, 'encrypt')
    return redirect(url_for('show_form', message=message, encrypted=transformed))

@application.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted = request.form['encrypted']
    transformed = transform(encrypted, 'decrypt')
    return redirect(url_for('show_form', message=transformed, encrypted=encrypted))


def transform(message, action, key=3):
    newMessage = ''
    for character in message:
        position = alphabet.find(character)
        if position >= 0:
            if 'encrypt' == action:
                new_position = (position + key) % 55
            else:
                new_position = (position - key) % 55
            new_character = alphabet[new_position]
            newMessage += new_character
        else:
            newMessage += character
    return newMessage


if __name__ == "__main__":
    application.run()
