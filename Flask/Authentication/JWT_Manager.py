import jwt

class JWTManager:
    def __init__(self, private_key_path, public_key_path):
        with open(private_key_path, "r") as file:
            self.private_key = file.read()

        with open(public_key_path, "r") as file:
            self.public_key = file.read()

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm="RS256")
            return encoded
        except Exception as e:
            print(f"Encode error: {e}")
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, 
                                 self.public_key, 
                                 algorithms=["RS256"])
            return decoded
        except Exception as e:
            print(f"Decode error: {e}")
            return None
