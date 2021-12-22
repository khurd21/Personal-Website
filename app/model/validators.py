from flask import flash


class MessageValidate:

    def __init__(self):
        self.NAME = 'NAME'
        self.EMAIL = 'EMAIL'
        self.MESSAGE = 'MESSAGE'


    def validate(self, items):
        return self.validate_name(items[self.NAME]) and self.validate_email(items[self.EMAIL]) \
            and self.validate_message(items[self.MESSAGE])


    def validate_name(self, name):

        if len(name) >= 32:
            flash('Name cannot exceed 32 characters.')
            return False

        if name == '':
            flash('Name cannot be empty')
            return False

        return True


    def validate_email(self, email):
        if len(email) >= 32:
            flash('Email cannot exceed 32 characters.')
            return False

        if email == '':
            flash('Email cannot be empty')
            return False

        if '@' in email and email[0] != '@':
            email = email.split('@')[1]
            if '.' in email and email[0] != '.':
                email = email.split('.')[1]
                if email != '':
                    return True

        flash('Invalid email format.')
        return False

    
    def validate_message(self, message):
        if len(message) >= 1028:
            flash('Message cannot exceed 1028 characters')
            return False
        
        if message == '':
            flash('Message cannot be empty')
            return False

        return True