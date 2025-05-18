import flet as ft
from . import agents_dashboard_functions

# CAMPO DE TEXTO PARA NOME DO AGENTE
name_textfield = ft.TextField(label="Nome", border_color=ft.Colors.PRIMARY, dense=True)

# CAMPO PARA NOME DO MODELO
model_dropdown = ft.Dropdown(border_color=ft.Colors.PRIMARY, label="Modelo", expand=True)

# CAMPO PARA SELEÇÃO DA FERRAMENTA A SER USADA
tools_dropdown = ft.Dropdown(
    border_color=ft.Colors.PRIMARY,
    label="Ferramentas",
    expand=True,
    options=[
        ft.DropdownOption(
            key="nenhuma",
            content=ft.Text(
                value="nenuma",
            ),
        ),
        ft.DropdownOption(
            key="google_search",
            content=ft.Text(
                value="google_search",
            ),
        ),
    ]
)

# CAMPO PARA ADICIONAR DESCRIÇÃO DO AGENTE
description_textfield = ft.TextField(label="Descrição", border_color=ft.Colors.PRIMARY, dense=True)

# CAMPO PARA ADICIONAR AS INSTRUÇÕES QUE O AGENTE DEVE SEGUIR
instruction_textfield = ft.TextField(label="Instruções", border_color=ft.Colors.PRIMARY, dense=True, multiline=True, max_lines=5)

# DIÁLOGO PARA ESCOLHA DO MODO DE CRIAÇÃO DE AGENTES (MANUAL OU AUTOMÁTICA)
agents_creation_mode_dialog = ft.AlertDialog(
    title=ft.Text("Novo Agente"),
    content=ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                icon=ft.Icons.ADD,
                text="Adicionar",
                on_click=agents_dashboard_functions.open_add_new_agent_dialog,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.GREEN_600,
                    color=ft.Colors.WHITE,
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=4,
                ),
            ),
            ft.ElevatedButton(
                icon=ft.Icons.AUTO_AWESOME,
                text="Auto Adicionar",
                on_click=agents_dashboard_functions.open_agent_auto_creattion_dialog,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_600,
                    color=ft.Colors.WHITE,
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=4,
                ),
            ),
        ]
    ),
)

# CAIXA DE DIÁLOGO PARA GERAR NOVO AGENTE (MANUAL)
new_agent_dialog = ft.AlertDialog(
    modal=True,
    title=ft.Text("Novo Agente"),
    content=ft.Container(
        padding=10,
        width=500,
        content=ft.Column(
            tight=True,
            spacing=8,
            controls=[
                name_textfield,
                model_dropdown,
                tools_dropdown,
                description_textfield,
                instruction_textfield,
            ]
        )
    ),
    actions=[
        ft.TextButton("Confirmar", on_click=agents_dashboard_functions.confirm),
        ft.TextButton("Cancelar", on_click=lambda e: agents_dashboard_functions.close_dialog(event=e, dialog=new_agent_dialog)),
    ],
)

# CAMPO DE TEXTO PARA INSERIR PROMPT PARA GERAÇÃO AUTOMATIZADA DE AGENTES
prompt_autogeneration_textfield = ft.TextField(multiline=True, max_lines=8, min_lines=8)

# DIÁLOGO PARA CRIAÇÃO DE AGENTES POR GERAÇÃO AUTOMATIZADA
auto_new_agent_dialog = ft.AlertDialog(
    modal=True,
    title=ft.Text("Auto Criação"),
    content=ft.Container(
        width=500,
        content=prompt_autogeneration_textfield,
    ),
    actions=[
        ft.TextButton("Confirmar", on_click=agents_dashboard_functions.confirm_agent_generation),
        ft.TextButton("Cancelar", on_click=lambda e: agents_dashboard_functions.close_dialog(event=e, dialog=new_agent_dialog)),
    ],
)

# DIÁLOGO PARA CONFIRMAR EXCLUSÃO DE AGENTE
delete_agent_dialog = ft.AlertDialog(
    modal=True,
    title=ft.Text("Deletar Agente"),
    content=ft.Text("Você quer realmente continuar a ação?"),
    actions=[
        ft.TextButton("Confirmar", on_click=agents_dashboard_functions.delete_agent),
        ft.TextButton("Cancelar", on_click=lambda e: agents_dashboard_functions.close_dialog(event=e, dialog=delete_agent_dialog)),
    ],
)

# ÁREA PARA EXIBIR DESCRIÇÃO DOS AGENTES
agents_area = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)

# BARRA INFERIOR PARA INSERIR BOTÕES NA ÁREA DOS AGENTES
buttons_bar = ft.Container(
    bgcolor=ft.Colors.PRIMARY_CONTAINER,
    border_radius=ft.border_radius.all(50),
    padding=10,
)

# BOTÃO ADICIONAR AGENTE
button = ft.ElevatedButton(
    icon=ft.Icons.ADD,
    text="Adicionar Agente",
    on_click=agents_dashboard_functions.open_agents_creation_mode_dialog,
    style=ft.ButtonStyle(icon_size=16, text_style=ft.TextStyle(size=16), padding=20),
)

# INSERINDO BOTÃO NA BARRA DE BOTÕES
buttons_bar.content = ft.Row(
    alignment=ft.MainAxisAlignment.END,
    controls=[
        button
    ]
)