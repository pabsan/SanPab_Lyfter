import jwt

class JWT_Manager:
    def __init__(self, secret, algorithm):
        self.secret = secret
        self.algorithm = algorithm

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.secret, self.algorithm)
            return encoded
        except:
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.secret, self.algorithm)
            return decoded
        except:
            return None
