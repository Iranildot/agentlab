import flet as ft
import utils.app_settings_functions as settings_functions
import dashboards.prompt.prompt_dashboard_functions as prompt_dashboard_functions

# BARRA DE MENU
menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.SECONDARY_CONTAINER,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Arquivo"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Limpar prompt"),
                        leading=ft.Icon(ft.Icons.CLEANING_SERVICES),
                        on_click=prompt_dashboard_functions.clear_chat_area,
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("Configurações"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Tema"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Claro"),
                                leading=ft.Icon(ft.Icons.LIGHT_MODE),
                                on_click=lambda e: settings_functions.set_theme(event=e, theme=ft.ThemeMode.LIGHT),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Escuro"),
                                leading=ft.Icon(ft.Icons.DARK_MODE),
                                on_click=lambda e: settings_functions.set_theme(event=e, theme=ft.ThemeMode.DARK),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Sistema"),
                                leading=ft.Icon(ft.Icons.SETTINGS_BRIGHTNESS),
                                on_click=lambda e: settings_functions.set_theme(event=e, theme=ft.ThemeMode.SYSTEM),
                            ),
                        ],
                    )
                ],
            ),
        ],
    )