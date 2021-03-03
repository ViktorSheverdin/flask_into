from random import randrange
from flask import Flask
app = Flask(__name__)

random_number = randrange(10)


@app.route("/")
def main_page():
    return "<h1>Guess number</h1>"


@app.route("/<int:number>")
def check_number(number):
    if number > random_number:
        return "<b>Too High</>"
    elif number < random_number:
        return "<b>Too Low</>"
    else:
        # random_number = randrange(10)
        return f"<h1>You are correct! The number is {random_number}</h1>"
        # app.route("/")


if __name__ == "__main__":
    app.run(debug=True)
