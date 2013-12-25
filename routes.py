from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input')
def input():
    return render_template('enterInfo.html', error=None)

@app.route('/input_response', methods=['GET', 'POST'])
def input_response():
    if request.method == 'POST':
        inputs = request.form.keys()
        if not ('recipient' in inputs and 'message' in inputs 
                and 'background' in inputs and 'sender' in inputs):
            return render_template('enterInfo.html',
                                   error="You must fill in all fields")
        recipient = request.form['recipient']
        sender = request.form['sender']
        message = request.form['message']
        background = request.form['background']
        return render_template('card.html', name=recipient,
                               msg=message, bg=background, sender=sender)

app.debug = True
