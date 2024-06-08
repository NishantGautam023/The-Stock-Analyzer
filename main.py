import openai
from flask import Flask, render_template



app  = Flask(__name__)
app.config.from_object("settings")

openai.api_key = app.config['OPENAI_API_KEY']


@app.route("/", methods=["GET", "POST"])
def render_home():
    return render_template('index.html')


@app.route('/ask-ai')
def ask_openai():
    # Todo: Learn how to create assistants and Thread Objects: https://platform.openai.com/docs/assistants/overview
    return "<h1>OpenAI Loading ... </h>1"

if __name__ == '__main__':
    app.run(
        host = app.config.get('HOST'),
        port = app.config.get('PORT')
    )