from wtforms.validators import ValidationError
import re


class StrongPassword:
    """Custom validator for strong passwords"""
    
    def __init__(self, message=None):
        if not message:
            message = 'Password must contain at least one uppercase letter, one lowercase letter, and one number.'
        self.message = message
    
    def __call__(self, form, field):
        password = field.data
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError(self.message)
        if not re.search(r'[a-z]', password):
            raise ValidationError(self.message)
        if not re.search(r'\d', password):
            raise ValidationError(self.message)


class NoSpecialChars:
    """Validator to prevent special characters in usernames"""
    
    def __init__(self, message=None):
        if not message:
            message = 'Username can only contain letters, numbers, and underscores.'
        self.message = message
    
    def __call__(self, form, field):
        if not re.match(r'^[a-zA-Z0-9_]+$', field.data):
            raise ValidationError(self.message)