import flet as ft
from . import agents_controls
import state
import json
import utils.google_adk_manager

# DELETA AGENTE
def delete_agent(event, index:int):
    def confirm():
        state.agents.delete_agent(index=index)
        load_agents()
        agents_controls.agents_area.update()
        page.close(agents_controls.delete_agent_dialog)

    page = event.control.page
    page.open(agents_controls.delete_agent_dialog)
    agents_controls.delete_agent_dialog.actions[0].on_click = lambda e: confirm()

# CARREGA DESCRIÇÃO DE AGENTES NA ÁREA DE AGENTES
def load_agents():
    agents_controls.agents_area.controls = []

    index = 0
    for agent in state.agents.agents:
        agents_controls.agents_area.controls.append(
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.SECONDARY_CONTAINER,
                        border_radius=20,
                        padding=20,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(agent["name"], size=20, weight=ft.FontWeight.BOLD),
                                        ft.Container(expand=True),
                                        ft.IconButton(ft.Icons.DELETE_FOREVER, on_click=lambda e, index=index: delete_agent(event=e, index=index))
                                    ]
                                ),
                                ft.Divider(color=ft.Colors.SECONDARY),
                                ft.Row(
                                    controls=[
                                        ft.Text("Modelo:", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text(agent["model"], size=16),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Ferramentas:", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text(agent["tools"], size=16),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Descrição:", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text(agent["description"], size=16),
                                    ]
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Instrução:", size=16, weight=ft.FontWeight.BOLD, no_wrap=False),
                                        ft.Text(agent["instruction"], size=16),
                                    ]
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        index += 1

# ADICIONAR AGENTES (MANUAL)
def add_agent():

    name = agents_controls.name_textfield.value
    model = agents_controls.model_dropdown.value
    tools = agents_controls.tools_dropdown.value
    description = agents_controls.description_textfield.value
    instruction = agents_controls.instruction_textfield.value
    
    state.agents.add_agent(name=name, model=model, tools=tools, instruction=instruction, description=description)
    load_agents()
    agents_controls.agents_area.update()

# FECHA CAIXAS DE DIÁLOGOS
def close_dialog(event, dialog):
    page = event.control.page
    page.close(dialog)

# CONFIRMA CRIAÇÃO DE AGENTE (MANUAL)
def confirm(event):
    page = event.control.page
    add_agent()
    page.close(agents_controls.new_agent_dialog)

# ABRE DIÁLOGO DE CRIAÇÃO DE AGENTES (MANUAL)
def open_add_new_agent_dialog(event):
    page = event.control.page
    page.close(agents_controls.agents_creation_mode_dialog)

    models_options = []
    models = []

    with open("./storage/data/models_name.json", "r") as file:
        models = json.load(file)

    for model in models:
        models_options.append(
            ft.DropdownOption(
                key=model,
                content=ft.Text(
                    value=model,
                ),
            )
        )
    agents_controls.model_dropdown.options = models_options
    page.open(agents_controls.new_agent_dialog)

# CRIAÇÃO DE AGENTES POR IA
def confirm_agent_generation(event):
    page = event.control.page
    agent = utils.google_adk_manager.create_agent(
        "auto_creation_agentlab_agent",
        instruction="""
Você é um agente especializado em criar outros agentes.
A ÚNICA resposta que você TEM que fornecer é uma lista de dicts (No formato JSON válido) e SOMENTE ISSO.
Cada dict é uma configuração de um agente.
Capriche nas instruções (CRIE SOLUÇÕES COMPLETAS) de cada agente a fim de que eles desempenhem suas funções com excelêencia, baseado nas necessidades do usuário.
Cada agente deve segir uma ordem correta na lista, pois um precisa executar suas instruções primeiro para poder passar para os seguintes.
A chave name deve ser escrita sem espaços em branco ou mesmo caracteres especiais (Com excesseção do _), use apenas [az-AZ] e [1-9]
A chave tools tem apenas dois valores possíveis: nenhuma ou google_search.
Vou te passar uma lista de models que você pode usar para a opção model.
A descrição deve ser siples e explicativa do que o agente faz.

###############

LISTA DE MODELOS:

[
    "gemini-2.0-flash",
]

###############

EXEMPLO DE SAÍDA:

[
    {
        "name": "agente_buscador",
        "model": "gemini-2.0-flash",
        "tools": "google_search",
        "instruction": "Você é um agente especializado em busca. Busque 5 notícias relevantes sobre o tema informado. Use o google_search para fazer a pesquisa. Seja criterioso na seleção, selecione apenas as notícias sobre assuntos que mais se repetem.",
        "description": ""
    },
    {
        "name": "agente_redator",
        "model": "gemini-2.0-flash",
        "tools": "nenhuma",
        "instruction": "Você é um agente redator, espeecializado em fazer redações voltadas para o instagram, mais especificamente, para público jovem entre 18 e 30 anos. Tenha uma escrita mais descontraída.",
        "description": ""
    },
    {
        "name": "agente_revisor",
        "model": "gemini-2.0-flash",
        "tools": "nenhuma",
        "instruction": "Você é um agente especializado em fazer correções ortográficos e de concordância.",
        "description": ""
    }
]

###############
""",)
    response = utils.google_adk_manager.call_agent(agent=agent, text_message=agents_controls.prompt_autogeneration_textfield.value)
    lines = response.splitlines()
    json_data = "\n".join(lines[1:-1])
    dados = json.loads(json_data)

    state.agents.agents = dados
    state.agents.save_agents()

    page.close(agents_controls.auto_new_agent_dialog)
    load_agents()
    page.update()

# ABRE DIÁLOGO DE CRIAÇÃO AUTOMÁTICA DE AGENTES
def open_agent_auto_creattion_dialog(event):
    page = event.control.page
    page.close(agents_controls.agents_creation_mode_dialog)
    page.open(agents_controls.auto_new_agent_dialog)

# ABRE DIÁLOGO PARA ESCOLHA DO MÉTODO DE CRIAÇÃO DOS AGENTES (MANUAL OU AUTOMÁTICA)
def open_agents_creation_mode_dialog(event):

    page = event.control.page    
    page.open(agents_controls.agents_creation_mode_dialog)
