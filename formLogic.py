from wtforms import Form, StringField, validators, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length, URL


class CreateMessage(Form):
        """Send message to the board Form"""

        sender = StringField('Name: ', [
            Length(min=4, max=10, message=('Name should be 4-10 characters long')),
            DataRequired(message="Name is missing?")
            ])

        title = StringField('Title: ', [
            Length(min=1, max=20, message=('Title should have between 1-20 characters')),
            DataRequired(message=('Title is missingno?'))
        ])

        content = TextAreaField('Content: ', [
            Length(min=1, max=128, message=('Content can be max 128 characters!')),
            DataRequired(message=('You have nothing to say?'))
        ])

        url = StringField('URL: ', [
            URL()
        ])

        submit = SubmitField('Send')

class ListMessages():

    def __init__(self, attributes, format=None):
        self.name = attributes.get('sender')
        self.title = attributes.get('title')
        self.content = attributes.get('content')
        
    def printMessage(self, format=None):
        
        messageData = [self.name, self.title, self.content, self.format]

        if format is None:
            print('listAllMessagesInBoard')
            return messageData
        else:
            print('exportMessages!')
            return 'Some'