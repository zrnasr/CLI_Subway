from user.models import User

class StateManager:
    __routes = []
    __user: None | User = None

    @classmethod
    def login_status(cls) -> bool:
        return bool(cls.__user)

    
    @classmethod
    def add_route_name(cls, name: str) -> None:
        if not len(cls.__routes) or cls.__routes[-1] != name:
            cls.__routes.append(name)

    @classmethod
    def delete_last_route_name(cls) -> None:
        cls.__routes.pop()

    @classmethod
    def set_user(cls, user: User) -> None:
        cls.__user = user

    @classmethod
    def get_user(cls) -> User:
        return cls.__user

    @classmethod
    def logout(cls) -> None:
        cls.__user = None
