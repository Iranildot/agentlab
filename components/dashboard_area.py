import flet as ft
from dashboards.prompt.prompt_dashboard import prompt_dashboard

# ÁREA QUE COMPORTA AS ABAS DE NAVEGAÇÃO (PROMPT OU AGENTES)
area = ft.Column(
    expand=True,
    spacing=10,
    controls=prompt_dashboard
)