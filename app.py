from flask import Flask, render_template, request, flash
from formLogic import CreateMessage, ListMessages

app = Flask(__name__,
            template_folder="templates")

totalMessages = 0

def addMessageCount(value):
    global totalMessages
    totalMessages += value

messagesInBoard = ListMessages()


@app.route("/", methods=['GET', 'POST'])
def home():
    """Serve message form."""
    sendMessageForm = CreateMessage()
    if request.method == 'POST':
        #if sendMessageForm.validate():
        print('Message sent!')
        messagesInBoard.printMessage()
        addMessageCount(1)
    return render_template("main.html",
                            form=sendMessageForm,
                            count=totalMessages)

if __name__ == '__main__':
    app.secret_key = 'notSoSecret'
    app.run(debug = True)