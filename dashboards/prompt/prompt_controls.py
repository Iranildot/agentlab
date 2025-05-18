import flet as ft
import utils.google_adk_manager as google_adk_manager

# ÁREA DE CHAT
chat_area = ft.Column(
    spacing=10,
    scroll=ft.ScrollMode.ALWAYS
)

# CAMPO DE TEXTO (PARA ESCREVER OS PROMPTS)
text_field = ft.TextField(
    border_color=ft.Colors.PRIMARY,
    expand=True,
    hint_text="Digite sua mensagem...",
    multiline=True,
    max_lines=8
)

# BOTÃO DE ENVIAR
button = ft.IconButton(
    icon=ft.Icons.SEND,
    tooltip="Enviar (ctrl + enter)",
    visible=True,
    on_click=lambda e: google_adk_manager.send_message(text_field.value)
)

# WIDGET DE CARREGAMENTO
spinner = ft.ProgressRing(
    width=40,
    height=40,
    stroke_width=3,
    visible=False,
)