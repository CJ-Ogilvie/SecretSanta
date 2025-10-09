import smtplib
from get_secure_data import get_email_address, get_phone_number, get_email_password


def _get_target_domain(name: str) -> str:
    return "sms.sasktel.com"  # Hard-coded for now, all use cases are currently on Sasktel

def _get_target_address(name: str) -> str:
    address = f"{get_phone_number(name)}@{_get_target_domain(name)}"
    print(f"Retrieved target address: {address}")
    return address

def _get_smtp_host() -> str:
    return "smtp.gmail.com"

def _get_smtp_port() -> int:
    return 587


class _EmailToTextConnection:

    def __init__(self):
        self.server = smtplib.SMTP(_get_smtp_host(), _get_smtp_port())
        self.server.starttls()
        self.email = get_email_address()
        self.server.login(self.email, get_email_password())


    def __del__(self):
        self.server.quit()

    def send_message(self, message: str, name: str):
        target = _get_target_address(name)
        self.server.sendmail(self.email, target, message)



MessageConnection: _EmailToTextConnection = None

def send_message(message: str, name: str) -> None:
    global MessageConnection
    if MessageConnection is None:
        print("Initializing message connection")
        MessageConnection = _EmailToTextConnection()
    print(f"Sending message to {name}")
    MessageConnection.send_message(message, name)
    print("Message send complete.")


if __name__ == "__main__":
    # Send test text to self
    send_message("test", "C.J.")
