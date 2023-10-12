from .router import Router, Route, CallBack
from .state import StateManager
from user.views import User

router = Router(
    Route("Main", description="Metro Project", epilog="Last Update: 2023-10-12 02:00", children= [
        Route("Register", CallBack("register", "user.views"), description= "The password should contain a-z, 0-9, and at least 8 characters", condition= lambda : not StateManager.login_status()),
        Route("Login", CallBack("login", "user.views"), condition= lambda: not StateManager.login_status()),
        Route("Administrator", children= [
            Route("Register", CallBack("register", "user.views"), description= "The password must contain a-z, 0-9, and at least 8 characters", condition= lambda: not StateManager.login_status()),
            Route("Login", CallBack("login", "user.views"), condition= lambda: not StateManager.login_status()),
        ]),
        Route("Exit"),
    ])
)