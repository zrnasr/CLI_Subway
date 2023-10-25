from .router import Router, Route, CallBack
from core.state import StateManager

user_view = "user.views"
ticket_view = "ticket.views"

router = Router(
    Route("Main", description="Metro Project", epilog="Last Update: 2023-10-12 02:00", children= [
        Route("Register", CallBack("register", user_view), description= "The password should contain a-z, 0-9, and at least 8 characters", condition= lambda : not StateManager.login_status()),
        Route("Login", CallBack("login", user_view), condition= lambda: not StateManager.login_status()),
        Route("Account", condition= StateManager.login_status, children= [
            Route("Balance", CallBack("balance", user_view)),
            Route("Deposit", CallBack("deposit", user_view)),
        ]),
        Route("Ticket", condition= StateManager.login_status, children= [
            Route("Chargeable", CallBack("buy_chargeable", ticket_view)),
            Route("Disposable", CallBack("buy_disposable", ticket_view)),
            Route("Charge Chargeable Ticket", CallBack("charge_chargeable_ticket", ticket_view)),
        ]),
        Route("Administrator", children= [
            Route("Register", CallBack("register", user_view), condition= lambda: not StateManager.login_status()),
            Route("Login", CallBack("login", user_view), condition= lambda: not StateManager.login_status()),
            Route("ban_user", CallBack("ban_user", user_view), condition= StateManager.login_status),
        ]),
        Route("Logout", CallBack("logout", user_view)),
    ])
)