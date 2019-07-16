from flask import Flask, render_template, request
from formLogic import CreateMessage, ListMessages

app = Flask(__name__,
            template_folder="templates")

totalMessages = 0
allMessages = []

def addMessageCount(value):
    global totalMessages
    totalMessages += value

@app.route("/", methods=['GET', 'POST'])
def home():
    """Serve message form."""
    sendMessageForm = CreateMessage()
    msgBoardData = []
    if request.method == 'POST':
        thisMessage = CreateMessage(request.form)
        if thisMessage.validate():
            sentMessage = ListMessages(request.form)
            allMessages.append(sentMessage)
            addMessageCount(1)
            msgBoardData = allMessages
        else:
            return render_template("main.html",
                                form=thisMessage,
                                count=totalMessages,
                                msgBoard=allMessages)
    return render_template("main.html",
                            form=sendMessageForm,
                            count=totalMessages,
                            msgBoard=msgBoardData)

if __name__ == '__main__':
    app.secret_key = 'notSoSecret'
    app.run(debug = True)