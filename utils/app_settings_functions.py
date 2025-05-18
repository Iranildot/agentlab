import flet as ft

# AJUSTAR TEMA DO APP
def set_theme(event, theme:ft.ThemeMode):

    page: ft.Page = event.control.page

    if theme == ft.ThemeMode.LIGHT: # CLARO
        page.theme_mode = ft.ThemeMode.LIGHT
    elif theme == ft.ThemeMode.DARK: # ESCURO
        page.theme_mode = ft.ThemeMode.DARK
    else: # SISTEMA
        page.theme_mode = ft.ThemeMode.SYSTEM
    
    page.update()