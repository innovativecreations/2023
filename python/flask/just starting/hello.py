from flask import Flask

app = Flask(__name__)


def make_bold(f):
    def bolder():
        txt = f()
        return f'<b>{txt}</b>'

    return bolder


def make_underlined(f):
    def underline():
        txt = f()
        return f'<u>{txt}</u>'

    return underline


def make_emphasis(f):
    def emphasis():
        txt = f()
        return f'<em>{txt}</em>'

    return emphasis


@app.route("/")
def home():
    return "Hello!"


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bhaag!"


if __name__ == "__main__":
    app.run(debug=True)
