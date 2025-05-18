from . import prompt_controls

# FUNÇÃO PARA LIMPAR ÁREA DE CHAT
def clear_chat_area(event):
    page = event.control.page
    prompt_controls.chat_area.controls = []
    prompt_controls.chat_area.update()