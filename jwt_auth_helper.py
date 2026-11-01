import datetime
from typing import Dict, Any, Optional
import jwt

class JWTAuthHelper:
    """A utility class for generating and verifying JSON Web Tokens (JWT)."""
    
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def generate_token(self, payload: Dict[str, Any], expiry_minutes: int = 30) -> str:
        """Generates a signed JWT token with an expiration time."""
        data = payload.copy()
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=expiry_minutes)
        data.update({"exp": expiration})
        
        token = jwt.encode(data, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verifies a JWT token and returns the decoded payload if valid."""
        try:
            decoded_payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
            return None
        except jwt.InvalidTokenError:
            print("Invalid token signature.")
            return None


# --- Example Usage ---
if __name__ == "__main__":
    # Requires: pip install PyJWT
    helper = JWTAuthHelper(secret_key="super-secret-key-change-me")
    
    user_data = {"user_id": 42, "role": "Developer"}
    token = helper.generate_token(user_data, expiry_minutes=15)
    print("Generated Token:", token[:30] + "...")
    
    verified_payload = helper.verify_token(token)
    print("Verified Payload:", verified_payload)
