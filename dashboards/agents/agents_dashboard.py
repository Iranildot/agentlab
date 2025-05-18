import flet as ft
from . import agents_controls, agents_dashboard_functions

# DEFINE OS WIDGETS DA ÁREA DE CRIAÇÃO DE AGENTES
agents_dashboard = [
    agents_controls.agents_area,
    agents_controls.buttons_bar # ÁREA DE BOTÃO CRIAR AGENTE
]

agents_dashboard_functions.load_agents() # CARREGA AGENTES GUARDADOS NO (SSD/HD)