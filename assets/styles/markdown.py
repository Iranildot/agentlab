import flet as ft

# CONJUNTO DE ESTILOS MARKDOWN

style_sheet = ft.MarkdownStyleSheet(
    # TÍTULOS
    h1_text_style=ft.TextStyle(size=42, weight=ft.FontWeight.BOLD),
    h1_padding=ft.padding.symmetric(vertical=12, horizontal=16),
    h2_text_style=ft.TextStyle(size=34, weight=ft.FontWeight.BOLD),
    h2_padding=ft.padding.symmetric(vertical=10, horizontal=14),
    h3_text_style=ft.TextStyle(size=28, weight=ft.FontWeight.W_600),
    h3_padding=ft.padding.symmetric(vertical=8, horizontal=12),
    h4_text_style=ft.TextStyle(size=24, weight=ft.FontWeight.W_500),
    h4_padding=ft.padding.symmetric(vertical=6, horizontal=10),
    h5_text_style=ft.TextStyle(size=20, weight=ft.FontWeight.W_500),
    h5_padding=ft.padding.symmetric(vertical=4, horizontal=8),
    h6_text_style=ft.TextStyle(size=18, weight=ft.FontWeight.W_500),
    h6_padding=ft.padding.symmetric(vertical=2, horizontal=6),

    # PARÁGRAFOS
    p_text_style=ft.TextStyle(size=18),
    p_padding=ft.padding.only(top=6, bottom=6),

    code_text_style=ft.TextStyle(
        size=17,
        weight=ft.FontWeight.BOLD,
    ),

    # CITAÇÕES
    blockquote_text_style=ft.TextStyle(size=18, italic=True),
    blockquote_padding=ft.padding.symmetric(vertical=8, horizontal=16),

    # LISTAS
    list_bullet_text_style=ft.TextStyle(size=18),
    list_bullet_padding=ft.padding.only(left=16),

    # TABELAS
    table_padding=ft.padding.all(10),
    table_cells_padding=ft.padding.symmetric(vertical=6, horizontal=10),

    # LINHA HORIZONTAL
    horizontal_rule_decoration=ft.BoxDecoration(
        border=ft.Border(bottom=ft.BorderSide(width=2))
    )
)

code_style_sheet = ft.MarkdownStyleSheet(
    code_text_style=ft.TextStyle(
        size=17,
        weight=ft.FontWeight.BOLD,
    ),
)