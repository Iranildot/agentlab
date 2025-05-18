import flet as ft
from components import rail
from components import dashboard_area
from components import menubar
from utils import apikey_manager
from utils import google_adk_manager
from dashboards.prompt import prompt_controls

class App:
    def __init__(self, page: ft.Page):

        self.page = page
        self.page.title = "AgentLab"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.page.on_keyboard_event = self.handle_key_event

        self.page.add(
            ft.Row(
                controls=[
                    menubar.menubar,
                ]
            ),
            ft.Row(
                [
                    rail.Control(),
                    ft.VerticalDivider(width=1),
                    ft.Container(
                        content=dashboard_area.area,
                        expand=True,
                        padding=20
                    ),
                ],
                expand=True,
            )
        )
    
    def handle_key_event(self, event: ft.KeyboardEvent):
        if event.key == "Enter" and event.ctrl:
            google_adk_manager.send_message(prompt_controls.text_field.value)

if __name__ == "__main__":
    ft.app(target=App)
