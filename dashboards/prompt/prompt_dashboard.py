import flet as ft
from . import prompt_controls

# WIDGETS QUE COMPONHE A ÁREA DE PROMPT (ÁREA DE INTERAÇÕES COM OS AGENTES)
prompt_dashboard = [
    ft.Container(
        content=prompt_controls.chat_area,
        expand=True,
        padding=10,
        bgcolor=ft.Colors.SURFACE,
        border_radius=10
    ),
    ft.Row(
        controls=[
            prompt_controls.text_field, # CAIXA DE TEXTO DO PROMPT
            prompt_controls.button, # BOTÃO ENVIA
            prompt_controls.spinner # WIDGET DE CARREGAMENTO
        ],
        spacing=10
    )
]