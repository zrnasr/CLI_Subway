from .router import Router, Route, CallBack
from .state import StateManager

router = Router(
    Route("Main", description="Metro Project", epilog="Last Update: 2023-10-12 02:00", children= [
        Route("Register", CallBack("register", "user.views"), description= "The password should contain a-z, 0-9, and at least 8 characters", condition= lambda : not StateManager.login_status()),
        Route("Login", CallBack("login", "user.views"), condition= lambda: not StateManager.login_status()),
        Route("Account", condition= StateManager.login_status, children= [
            Route("Balance", CallBack("balance", "user.views")),
            Route("Deposit", CallBack("deposit", "user.views")),
            Route("Withdraw", CallBack("withdraw", "user.views")),
        ]),
        Route("Ticket", condition= StateManager.login_status, children= [
            Route("Chargeble", CallBack("chargeble", "user.views")),
            Route("Disposable", CallBack("disposable", "user.views")),
            Route("Date Expirable", CallBack("date Expirable", "user.views")),
        ]),
        Route("Administrator", children= [
            Route("Register", CallBack("register", "user.views"), condition= lambda: not StateManager.login_status()),
            Route("Login", CallBack("login", "user.views"), condition= lambda: not StateManager.login_status()),
            Route("ban_user", CallBack("ban_user", "user.views"), condition= StateManager.login_status),
        ]),
        Route("Logout", CallBack("logout", "user.views")),
    ])
)