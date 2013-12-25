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
        if not 'background' in inputs: 
            return render_template('enterInfo.html',
                                   error="You must fill in all fields")
        recipient = request.form['recipient']
        sender = request.form['sender']
        message = request.form['message']
        background = request.form['background']
        if not recipient or not sender or not message:
            return render_template('enterInfo.html',
                                   error="You must fill in all fields")
        
        return render_template('card.html', name=recipient,
                               msg=message, bg=background, sender=sender)

if __name__ == '__main__':
    app.run()
