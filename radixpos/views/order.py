import flet as ft
from .view import MainView


def order_view(page: ft.Page):
    view = MainView(
        page,
        "/",
        [
            ft.Text("Hello, World!"),
            ft.Text("Hello, World!", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
        ],
    )

    return view
