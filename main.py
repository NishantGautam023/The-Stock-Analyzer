from flask import Flask, render_template
import os


app  = Flask(__name__)
app.config.from_object("settings")


@app.route("/", methods=["GET", "POST"])
def render_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host = app.config.get('HOST'),
        port = app.config.get('PORT')
    )