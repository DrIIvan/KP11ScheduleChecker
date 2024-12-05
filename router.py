import flet as ft
from flet_route import Routing, path
from pages.page_errorchecker import ErrorChecker


class Router:
    def __init__(self, page:ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=ErrorChecker().view)
        ]
        
        Routing(
            page=self.page,
            app_routes=self.app_routes
        )

        self.page.go(self.page.route)
