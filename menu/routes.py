from .router import Router, Route, CallBack
from .state import StateManager

router = Router(
    Route("Main", description="Metro Project", epilog="Last Update: 2023-10-12 02:00", children= [
        Route("Register", CallBack("login", "users.views"), description= "The password should contain a-z, 0-9, and at least 8 characters", condition= lambda : not StateManager.login_status()),
        Route("Login", condition= lambda: not StateManager.login_status()),
        Route("Administrator", children= [
            Route("Register", description= "The password must contain a-z, 0-9, and at least 8 characters", condition= lambda: not StateManager.login_status()),
            Route("Login", condition= lambda: not StateManager.login_status()),
        ]),
        Route("Exit"),
    ])
)