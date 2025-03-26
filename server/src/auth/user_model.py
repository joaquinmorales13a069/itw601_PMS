class User:
    def __init__(self, email, password):
        """
        User class that stores authentication credentials with email as the identifier
        and password for verification.
        """
        self.email = email
        self.password = password
