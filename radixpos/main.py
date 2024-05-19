import flet as ft
from views import home_view, order_view, prepare_view, payment_view, settings_view


def main(page: ft.Page):
    page.title = "RadixPOS"
    page.theme = ft.Theme(color_scheme_seed="2a7255")

    def route_change(e: ft.RouteChangeEvent):
        troute = ft.TemplateRoute(e.route)
        if troute.match("/"):
            page.views.clear()
            page.views.append(home_view(page))
        elif troute.match("/order"):
            page.views.append(order_view(page))
        elif troute.match("/prepare"):
            page.views.append(prepare_view(page))
        elif troute.match("/payment"):
            page.views.append(payment_view(page))
        elif troute.match("/settings"):
            page.views.append(settings_view(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        top_view.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")


def run(main):
    ft.app(main, view=ft.WEB_BROWSER, port=8000)


if __name__ == "__main__":
    run(main)
