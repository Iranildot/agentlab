import flet as ft
from utils import apikey_manager
import os

# ABRE DIÁLOGO PARA CADASTRAR CHAVE API
def open(page: ft.Page):

    def confirm():
        apikey_manager.set_apikey(textfield.value)
        page.close(apikey_dialog)

    textfield = ft.TextField(
        border_color=ft.Colors.PRIMARY,
        can_reveal_password=True,
        hint_text="Digite sua API Key",
        prefix_icon=ft.Icons.KEY,
        password=True,
        value=os.environ["GOOGLE_API_KEY"] or "",
        width=500,
    )

    apikey_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("API Key"),
        content=ft.Container(
            content=textfield,
            width=500
        ),
        actions=[
            ft.TextButton("Confirm", on_click=lambda e: confirm()),
            ft.TextButton("Cancel", on_click=lambda e: page.close(apikey_dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.open(apikey_dialog)
    apikey_dialog.open = True
    page.update()
