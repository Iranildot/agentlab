import flet as ft
from . import apikey_dialog
from dashboards.prompt.prompt_dashboard import prompt_dashboard
from dashboards.agents.agents_dashboard import agents_dashboard
from . import dashboard_area

# MENU DE NAVEGAÇÃO LATERAL (COM BOTÕES QUE REDIRECIONAM PARA AGENTES OU PARA ÁREA DE PROMPT)
class Control(ft.NavigationRail):
    def __init__(self, destinations = None, elevation = None, selected_index = None, extended = None, label_type = None, bgcolor = None, indicator_color = None, indicator_shape = None, leading = None, trailing = None, min_width = None, min_extended_width = None, group_alignment = None, selected_label_text_style = None, unselected_label_text_style = None, on_change = None, ref = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, visible = None, disabled = None, data = None, rtl = False):
        super().__init__(destinations, elevation, selected_index, extended, label_type, bgcolor, indicator_color, indicator_shape, leading, trailing, min_width, min_extended_width, group_alignment, selected_label_text_style, unselected_label_text_style, on_change, ref, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, rtl)

        self.extended=False
        self.selected_index=0
        self.label_type=ft.NavigationRailLabelType.ALL
        self.min_width=100
        min_extended_width=400
        self.leading=ft.FloatingActionButton(
            icon=ft.Icons.KEY, text="API Key", on_click=lambda e: apikey_dialog.open(page=self.page)
        )
        self.group_alignment=-0.9
        self.destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.CHAT_BUBBLE_OUTLINE_ROUNDED,
                selected_icon=ft.Icons.CHAT_BUBBLE_ROUNDED,
                label="Prompt",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SMART_TOY_OUTLINED),
                selected_icon=ft.Icon(ft.Icons.SMART_TOY),
                label="Agentes",
            ),
        ]
        self.on_change=self.__navigate

    # MÉTODO PARA NAVEGAÇÃO ENTRE ABAS
    def __navigate(self, event:ft.OptionalControlEventCallable):
        selected_index = event.control.selected_index
        match selected_index:
            case 0: # PROMPT
                dashboard_area.area.controls = prompt_dashboard
            case 1: # AGENTS
                dashboard_area.area.controls = agents_dashboard
        dashboard_area.area.update()
        
