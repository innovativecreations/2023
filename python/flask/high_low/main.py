from flask import Flask
import random

app = Flask(import_name=__name__)

no = random.randint(0,9)
# no = 5
@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1><br>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:a>")
def result(a):
    print(a)
    if a == no:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif a < no:
        return '<h1 style="color: cyan">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif a > no:
        return '<h1 style="color: red">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run()