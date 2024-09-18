from flask import Flask, render_template, request
import emoji

app = Flask(__name__)

# Dictionary of emojis and their meanings


# Generate a dictionary of emojis and their descriptions
emoji_dict = {e: emoji.demojize(e) for e in emoji.EMOJI_DATA.keys()}



@app.route('/', methods=['GET', 'POST'])
def index():
    meaning = None
    if request.method == 'POST':
        emoji = request.form.get('emoji')
        # Look up the meaning of the emoji
        meaning = emoji_dict.get(emoji, 'Emoji not found')
    return render_template('index.html', meaning=meaning)  # Only pass 'meaning' here

if __name__ == '__main__':
    app.run(debug=True)
