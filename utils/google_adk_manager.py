from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import assets.styles.markdown
import dashboards.prompt.prompt_controls as prompt_controls
import assets.styles
import flet as ft
import time
import state

# CHAMA AGENTE PARA OBTER RESPOSTAS
def call_agent(agent: Agent, text_message:str) -> str:

    session_service = InMemorySessionService()

    session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")

    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)

    content = types.Content(role="user", parts=[types.Part(text=text_message)])

    final_response = ""

    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text
    return final_response

# CRIAR AGENTE
def create_agent(name:str="gemini", model:str="gemini-2.0-flash", tools:list=[], instruction:str="", description:str=""):
    agent = Agent(
        name=name,
        model=model,
        description=description,
        tools=tools,
        instruction=instruction,
    )
    return agent

# AJUDA A FORMATAR A SAÍDA DO(S) AGENTE(S) RELACIONADA A ENTRADA DO USUÁRIO
def send_message(input_message:str):
    def chat_bubble(content:ft.Control, index:int):
        return ft.Container(
            content=content,
            alignment=[ft.alignment.center_right, ft.alignment.center_left][index],
            bgcolor=[ft.Colors.PRIMARY_CONTAINER, ft.Colors.SECONDARY_CONTAINER][index],
            border_radius=12,
            expand=False,
            padding=ft.padding.symmetric(20, 30),
            margin=6,
        )
    
    if input_message.strip(): # CASO USUÁRIO NÃO DIGITI NADA (NÃO EXECUTA O RESTANTE)
        prompt_controls.spinner.visible = True
        prompt_controls.button.visible = False
        prompt_controls.text_field.value = ""
        
        prompt_controls.chat_area.controls.append(chat_bubble(ft.Text(input_message, size=18), 0))
        prompt_controls.button.update()
        prompt_controls.text_field.update()
        prompt_controls.chat_area.update()
        prompt_controls.spinner.update()

        if state.agents.agents: # CASO USUÁRIO NÃO TENHA CADASTRADO NENHUM AGENTE
            
            response_message_cash = input_message
            for agent_settings in state.agents.agents:
                name = agent_settings["name"]
                model = agent_settings["model"]
                match agent_settings["tools"]:
                    case "google_search":
                        tools = [google_search]
                    case _:
                        tools = []
                description = agent_settings["description"]
                instruction = agent_settings["instruction"]
                response_message = f"##### {name}\n" + call_agent(create_agent(
                    name=name,
                    model=model,
                    tools=tools,
                    description=description,
                    instruction=instruction
                ), text_message=response_message_cash)

                markdown_control = ft.Markdown(
                    "",
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    code_theme=ft.MarkdownCodeTheme.AGATE,
                    md_style_sheet=assets.styles.markdown.style_sheet,
                    on_tap_link=lambda e: prompt_controls.chat_area.page.launch_url(e.data),
                    code_style_sheet=assets.styles.markdown.code_style_sheet
                )
                prompt_controls.chat_area.controls.append(chat_bubble(markdown_control, 1))
                for letter in response_message:
                    markdown_control.value += letter
                    prompt_controls.chat_area.scroll_to(-1)
                    prompt_controls.chat_area.update()
                    time.sleep(0.002)

                response_message_cash = response_message
        
        else: 
            prompt_controls.chat_area.controls.append(chat_bubble(ft.Text("Adicione pelo menos um agente, na aba agentes, para poder receber respostas.", size=18), 1))
        
        prompt_controls.spinner.visible = False
        prompt_controls.button.visible = True
        prompt_controls.button.update()
        prompt_controls.chat_area.update()
        prompt_controls.spinner.update()