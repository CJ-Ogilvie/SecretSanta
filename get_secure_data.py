import os

__email_address_env_key = "email_address"
__email_password_env_key = "email_password"
__phone_env_key_prefix = "phone_number_"  # Followed by name


def get_email_address() -> str:
    address = os.getenv(__email_address_env_key)
    print(f"Retrieved source email address: {address}")
    return os.getenv(__email_address_env_key)


def get_phone_number(name: str) -> str:
    number = os.getenv(f"{__phone_env_key_prefix}{name}")
    assert number is not None, (f"Phone number for name '{name}' is not defined in environment variables. "
                                f"Define as '{__phone_env_key_prefix}{name}' to use.")
    return number


def get_email_password() -> str:
    return os.getenv(__email_password_env_key)
