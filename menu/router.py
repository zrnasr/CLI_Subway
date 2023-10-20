from typing import Any, Callable
from .state import StateManager
from importlib import import_module

class CallBack:
    def __init__(self, function: str | Callable, package: None | str = None, *args, **kwargs):
        self.function = function
        self.package = package
        self.kwargs = kwargs
        self.args = args

#when does it call???
    def __call__(self, *args, **kwargs):
        self.function = getattr(import_module(self.package or __name__), self.function if isinstance(self.function, str) else self.function.__name__)
        self.function(*self.args, *args, **self.kwargs, **kwargs)
        #what is *self.args?


class Route:
    def __init__(self, name : str, callback: Callable | None = None, description: str | None = None, children: list["Route"] | None = None, condition: Callable = lambda: True, epilog : str | None = None):
        self.parent = None
        self.children = None
        self.condition = condition
        self.name = name
        self.callback = callback
        self.description = description
        self.epilog = epilog
        children and self._set_parent(children)

    
    def _set_parent(self, children):
        for child in children:
            child.parent = self
        self.children = children

    def _get_route(self) -> "Route":
        while True:
            try:
                print(self.description or " ", end= "\n\n")
                if children := [ child for child in self.children if child.condition()]:
                    for child in children:
                        child : Route  ### whats happening???
                        print(f" {children.index(child) + 1}. {child.name}")
                    print(f"\n 0. Back to '{self.parent.name}'" if self.parent else "\n 0. Exit")
                    print("\n" + (self.epilog or " "))

                    index = int(input("\n> ")) - 1
                    route = children[index] if index != -1 else self.parent


                    if not route:
                        if input("Do you want to exit ? [y|N] : ").strip().lower()[0] == "y":
                            print("Goodbye XD")
                            exit()
                        else:
                            continue
                    return route
                else:
                    print("\n" + (self.epilog or " "))
                    return self

            except(ValueError, IndexError, KeyboardInterrupt, AssertionError):
                input("Please enter valid number. \nPress Enter to continue ...")
                continue



    def __call__(self, *args, **kwargs):
        StateManager.add_route_name(self.name)
        route : Route = self._get_route()

        if self.parent == route:
            StateManager.delete_last_route_name()
            route()
        elif route.children:
            route()
        else:
            try:
                route.callback and route.callback(route)
            except Exception as e:
                print("Error!", e)
            input(f"\nPress Enter back to '{route.parent.name}' ...")

            StateManager.delete_last_route_name()
            route.parent()


class Router:
    def __init__(self, main_route : Route):
        self.main_route = main_route
        ...

    def __call__(self, *args: Any, **kwargs):
        self.main_route(*args, **kwargs)