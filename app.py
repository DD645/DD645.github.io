from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['message'] = "I'm thinking of a number between 1 and 100!"

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
        except ValueError:
            session['message'] = "Please enter a valid number!"
            return redirect(url_for('index'))

        number = session['number']
        if guess < number:
            session['message'] = "Too low! Try again."
        elif guess > number:
            session['message'] = "Too high! Try again."
        else:
            session['message'] = f"🎉 Congratulations! You guessed it! The number was {number}."
            session.pop('number')  # Reset the game

        return redirect(url_for('index'))

    return render_template('index.html', message=session.get('message'))

if __name__ == '__main__':
    app.run(debug=True)