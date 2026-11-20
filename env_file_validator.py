import os


def parse_env_file(filepath: str = ".env") -> dict[str, str]:
    """Parses KEY=VALUE pairs from an environment file, ignoring comments and blanks."""
    env_vars: dict[str, str] = {}
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Environment file '{filepath}' not found.")

    with open(filepath, "r", encoding="utf-8") as file:
        for line_num, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                print(f"Warning: Skipping malformed line {line_num}: {line}")
                continue
            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip().strip("'\"")

    return env_vars


def validate_required_keys(env_vars: dict[str, str], required_keys: list[str]) -> list[str]:
    """Returns a list of required keys that are missing or have empty values."""
    return [key for key in required_keys if not env_vars.get(key)]


if __name__ == "__main__":
    sample_env = "sample.env"
    with open(sample_env, "w", encoding="utf-8") as f:
        f.write("# Sample config\nAPP_ENV=development\nPORT=8000\nAPI_KEY=\n")

    parsed = parse_env_file(sample_env)
    missing = validate_required_keys(parsed, ["APP_ENV", "PORT", "API_KEY", "SECRET_KEY"])
    print("Parsed variables:", parsed)
    print("Missing or empty required keys:", missing)
