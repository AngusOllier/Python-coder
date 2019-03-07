from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

@app.route('/codec')
def codec():
    return render_template('decoder.html')


@app.route('/transform', methods=['POST'])
def do_codec():
    action = 'encode'
    transformed = transform(request.form['message'], action)
    return render_template('decoder.html', action=action, transformed=transformed)


def transform(message, action, key=3):
    newMessage = ''
    for character in message:
        position = alphabet.find(character)
        if 'encode' == action:
            new_position = (position + key) % 52
        else:
            new_position = (position - key) % 52
        new_character = alphabet[new_position]
        newMessage += new_character
        newMessage += character
    return newMessage


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
