from hashlib import sha256

from names import get_first_name, get_last_name

from src.model.user import User

EXAMPLE_COM = "example.com"


class DataUtils:

    @staticmethod
    def __generate_user() -> User:
        name = get_first_name()
        surname = get_last_name()
        email = f"{name}.{surname}@{EXAMPLE_COM}".lower()
        password = sha256(f"{name}{surname}{email}".encode("utf-8")).hexdigest()

        return User(name, surname, email, password)

    @staticmethod
    def generate_users(n: int = 5) -> list:
        return [DataUtils.__generate_user() for i in range(n)]
