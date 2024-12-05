import flet as ft
from router import Router


def main(page: ft.Page):

    # Выбор темы приложения.
    page.theme_mode = "dark"

    # Вызов класса адресации страниц.
    Router(page)


if __name__ == "__main__":
    ft.app(target=main)
