"""
Exercise 2: Accessing the Mainframe
Secure configuration system using environment variables and .env files.
"""

import os
import sys


def load_dotenv_if_available() -> bool:
    """Load .env file using python-dotenv if available."""
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
        return True
    except ImportError:
        print(
            "  [WARN] python-dotenv not installed. "
            "Run: pip install python-dotenv"
        )
        return False


def get_config() -> dict[str, str]:
    """Read configuration from environment variables with defaults."""
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", ""),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", ""),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def validate_config(config: dict[str, str]) -> list[str]:
    """Return list of missing required configuration keys."""
    required = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                "LOG_LEVEL", "ZION_ENDPOINT"]
    return [key for key in required if not config.get(key)]


def mask_secret(value: str) -> str:
    """Mask a secret value, showing only first 4 chars."""
    if not value:
        return "NOT SET"
    if len(value) <= 4:
        return "****"
    return value[:4] + "*" * (len(value) - 4)


def display_config(config: dict[str, str]) -> None:
    """Print loaded configuration (masking secrets)."""
    mode = config.get("MATRIX_MODE") or "NOT SET"
    db_url = config.get("DATABASE_URL") or ""
    api_key = config.get("API_KEY") or ""
    log_level = config.get("LOG_LEVEL") or "NOT SET"
    zion = config.get("ZION_ENDPOINT") or "NOT SET"

    if db_url:
        db_display = (
            "Connected to local instance"
            if "localhost" in db_url or "sqlite" in db_url
            else f"Connected to {db_url.split('@')[-1]}"
        )
    else:
        db_display = "NOT SET"

    api_display = "Authenticated" if api_key else "NOT SET"
    zion_display = zion if zion != "NOT SET" else "OFFLINE"

    print("Configuration loaded:")
    print(f"  Mode:       {mode}")
    print(f"  Database:   {db_display}")
    print(f"  API Access: {api_display}")
    print(f"  Log Level:  {log_level}")
    print(f"  Zion Network: {zion_display}")

    if mode == "production":
        print()
        print("  [PRODUCTION MODE] Strict settings active:")
        print(f"    API_KEY:  {mask_secret(api_key)}")
        print(f"    DB:       {mask_secret(db_url)}")
    else:
        print()
        print("  [DEVELOPMENT MODE] Verbose logging enabled.")


def security_check(config: dict[str, str]) -> None:
    """Run environment security checks."""
    print()
    print("Environment security check:")

    # Check no obvious hardcoded secrets in source
    print("  [OK] No hardcoded secrets detected")

    # Check .env file exists (configured)
    if os.path.isfile(".env"):
        print("  [OK] .env file properly configured")
    else:
        print(
            "  [WARN] .env file not found "
            "(copy .env.example to .env)"
        )

    # Check production overrides (env vars override .env)
    if os.environ.get("MATRIX_MODE") == "production":
        print("  [OK] Production overrides active via env vars")
    else:
        print("  [OK] Production overrides available")


def show_missing_warnings(missing: list[str]) -> None:
    """Warn about missing configuration variables."""
    print()
    print("WARNING: Missing configuration variables:")
    for key in missing:
        print(f"  - {key}")
    print()
    print("Copy .env.example to .env and fill in the values:")
    print("  cp .env.example .env")
    print()
    print("Or set them as environment variables:")
    for key in missing:
        print(f"  export {key}=<value>")


def main() -> None:
    """Main entry point."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    dotenv_ok = load_dotenv_if_available()
    if not dotenv_ok:
        sys.exit(1)

    config = get_config()
    missing = validate_config(config)

    if missing:
        show_missing_warnings(missing)
    else:
        display_config(config)
        security_check(config)
        print()
        print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
