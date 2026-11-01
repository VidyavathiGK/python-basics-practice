from typing import Dict, Any, List

class JSONSchemaValidator:
    """A lightweight schema validator for dictionary and JSON data."""
    
    def __init__(self, schema: Dict[str, Dict[str, Any]]):
        self.schema = schema

    def validate(self, data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validates input data against the defined schema rules.
        Returns a tuple of (is_valid, list_of_error_messages).
        """
        errors = []
        
        for field, rules in self.schema.items():
            # Check required fields
            if rules.get("required", False) and field not in data:
                errors.append(f"Missing required field: '{field}'")
                continue
                
            if field in data:
                value = data[field]
                expected_type = rules.get("type")
                
                # Check data type
                if expected_type and not isinstance(value, expected_type):
                    errors.append(f"Field '{field}' must be of type {expected_type.__name__}, got {type(value).__name__}")
                
                # Check choices / options
                allowed_choices = rules.get("choices")
                if allowed_choices and value not in allowed_choices:
                    errors.append(f"Field '{field}' has invalid value '{value}'. Allowed: {allowed_choices}")
                    
        return len(errors) == 0, errors


# --- Example Usage ---
if __name__ == "__main__":
    # Define validation rules
    user_schema = {
        "username": {"required": True, "type": str},
        "age": {"required": True, "type": int},
        "role": {"required": False, "type": str, "choices": ["Admin", "Developer", "Guest"]}
    }
    
    validator = JSONSchemaValidator(user_schema)
    
    # Test valid data
    valid_payload = {"username": "Vidyavathi", "age": 23, "role": "Developer"}
    is_ok, errs = validator.validate(valid_payload)
    print("Valid Payload Check:", is_ok, errs)
    
    # Test invalid data
    invalid_payload = {"username": "Coder", "age": "twenty", "role": "Superuser"}
    is_ok, errs = validator.validate(invalid_payload)
    print("Invalid Payload Check:", is_ok, errs)
