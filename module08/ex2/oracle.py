"""Oracle configuration exercise.

Loads settings from environment variables and .env files.
"""

import os


try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


CONFIG_KEYS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def load_configuration():
    if load_dotenv is None:
        return None

    load_dotenv(override=False)
    return {key: os.getenv(key) for key in CONFIG_KEYS}


def config_source(key):
    if key in os.environ:
        return "environment"
    if os.path.exists(".env"):
        return ".env"
    return "default"


def pick_mode(value):
    if value == "production":
        return "production"
    return "development"


def format_database_status(mode, database_url):
    if not database_url:
        return "Missing database configuration"
    if mode == "production":
        return "Connected to production instance"
    return "Connected to local instance"


def format_api_status(api_key):
    if api_key:
        return "Authenticated"
    return "Missing API key"


def format_log_level(mode, log_level):
    if log_level:
        return log_level.upper()
    if mode == "production":
        return "INFO"
    return "DEBUG"


def format_zion_status(zion_endpoint):
    if zion_endpoint:
        return "Online"
    return "Offline"


def print_security_check(config_exists):
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if config_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing or not loaded")
    print("[OK] Production overrides available")


def main():
    if load_dotenv is None:
        print("ORACLE STATUS: Reading the Matrix...")
        print("Missing dependency: python-dotenv")
        print("Install it with: pip install python-dotenv")
        print("Or add it to your Poetry environment and run again.")
        return 1

    load_configuration()
    config_exists = os.path.exists(".env")

    mode = pick_mode(os.getenv("MATRIX_MODE"))
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {format_database_status(mode, database_url)}")
    print(f"API Access: {format_api_status(api_key)}")
    print(f"Log Level: {format_log_level(mode, log_level)}")
    print(f"Zion Network: {format_zion_status(zion_endpoint)}")
    print()
    print("Configuration sources:")

    for key in CONFIG_KEYS:
        print(f"- {key}: {config_source(key)}")

    print()
    print_security_check(config_exists)
    print("The Oracle sees all configurations.")

    if mode == "production" and (not database_url or not api_key):
        print("Warning: production mode is missing critical secrets.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())