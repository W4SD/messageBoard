from flask import Flask, render_template
from formLogic import CreateMessage

app = Flask(__name__,
            template_folder="templates")

@app.route("/")
def home():
    """Serve message form."""
    sendMessageForm = CreateMessage()
    return render_template("messageForm.html", form=sendMessageForm)

if __name__ == '__main__':
   app.run(debug = True)