
class StateManager:
    __routes = []
    __user: None #| User = None

    @classmethod   #why not an usual method?
    def login_status(cls) -> bool:
        # return bool(cls.__user)
        return False
    
    @classmethod
    def add_route_name(cls, name: str) -> None:
        if not len(cls.__routes) or cls.__routes[-1] != name:
            cls.__routes.append(name)

    @classmethod
    def delete_last_route_name(cls) -> None:
        cls.__routes.pop()
