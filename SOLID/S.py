# 1. Single Responsibility Principle (SRP)
#
# Definition:
# A class should have only one reason to change, meaning it should have only one responsibility or purpose.
#
# Example: Suppose you have a User class that handles user data,
# sends email notifications, and logs user activities:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self):
        # logic to send an email
        pass

    def log_activity(self):
        # logic to log user activity
        pass

# This class violates SRP because it has multiple responsibilities:
# managing user data, sending emails, and logging activities.
# A better approach would be to separate these concerns:


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    def send_email(self, user):
        # logic to send an email
        pass

class ActivityLogger:
    def log_activity(self, user):
        # logic to log user activity
        pass

# Now, each class has a single responsibility, making the code easier to maintain and modify.
