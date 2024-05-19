import flet as ft


class SideMenuItem(ft.NavigationDrawerDestination):
    def __init__(self, route: str, label: str, icon: str, selected_icon: str):
        self.route = route
        super().__init__(label=label, icon=icon, selected_icon=selected_icon)


class SideMenu(ft.NavigationDrawer):
    def __init__(self, page: ft.Page, items: list[ft.Control]):
        self.page = page
        route = page.route

        self.routes = []
        controls = []
        for item in items:
            controls.append(item)
            if type(item) == SideMenuItem:
                self.routes.append(item.route)

        selected_index = self.routes.index(route)
        super().__init__(
            controls,
            selected_index=selected_index,
            on_change=self.change_route,
        )

    def change_route(self, e):
        self.page.go(self.routes[self.selected_index])


class MainView(ft.View):
    def __init__(self, page: ft.Page, route: str, controls: list[ft.Control]):
        appbar = ft.AppBar(
            title=ft.Text("RadixPOS"),
        )

        side_menu_items = [
            ft.Container(height=12),
            SideMenuItem(
                route="/",
                label="ホーム",
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
            ),
            ft.Divider(thickness=2),
            SideMenuItem(
                route="/order",
                label="注文モード",
                icon=ft.icons.SHOPPING_CART_OUTLINED,
                selected_icon=ft.icons.SHOPPING_CART,
            ),
            SideMenuItem(
                route="/prepare",
                label="準備モード",
                icon=ft.icons.KITCHEN_OUTLINED,
                selected_icon=ft.icons.KITCHEN,
            ),
            SideMenuItem(
                route="/payment",
                label="会計モード",
                icon=ft.icons.PAYMENTS_OUTLINED,
                selected_icon=ft.icons.PAYMENTS,
            ),
            ft.Divider(thickness=2),
            SideMenuItem(
                route="/settings",
                label="設定",
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
            ),
        ]

        drawer = SideMenu(
            page,
            side_menu_items,
        )

        super().__init__(route=route, appbar=appbar, drawer=drawer, controls=controls)
