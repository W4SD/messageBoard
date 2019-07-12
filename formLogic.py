from wtforms import Form, StringField, validators, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

class CreateMessage(Form):
        """Send message to the board Form"""

        sender = StringField('Name: ', [
            Length(min=4, max=10, message=('Name should be 4-10 characters long')),
            DataRequired(message=('Choose a viable name!'))
            ])

        title = StringField('Title: ', [
            Length(min=1, max=20, message=('A message should have title between 1-20 characters')),
            DataRequired(message=('Choose a good title'))
        ])

        content = TextAreaField('Content: ', [
            Length(min=1, max=128, message=('Content can be max 128 characters!')),
            DataRequired(message=('What say u?'))
        ])

        submit = SubmitField('Send')