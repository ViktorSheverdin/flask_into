from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello  {name} you are {number} years old!!!!"


def make_bold(function):
    def make_text_bold():
        return f"<b>{function()}</b>"
    return make_text_bold


def make_emphesised(function):
    def make_text_bold():
        return f"<em>{function()}</em>"
    return make_text_bold


def make_underlined(function):
    def make_text_bold():
        return f"<u>{function()}</u>"
    return make_text_bold


@app.route("/bye")
@make_bold
@make_emphesised
@make_underlined
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
