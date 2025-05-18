import keyring
import os
import json
from google import genai
import flet as ft

# CARREGAR CHAVE API GUARDADO NO SISTEMA DE SENHAS DO SO
def load_apikey():
    os.environ["GOOGLE_API_KEY"] = keyring.get_password("AGENTLAB", "GOOGLE_API_KEY")

    # CARREGA A LISTA DE MODELOS LLM
    try:
        if not os.path.exists("./storage/data/models_name.json"):
            models = []
            for model in genai.Client().models.list():
                name = model.name[7:]
                models.append(name)

            with open("./storage/data/models_name.json", "w") as file:
                json.dump(models, file, indent=4)
    except:
        ...

# GUARDA A CHAVE API NO SISTEMA DE SENHAS
def set_apikey(api_key:str):
    keyring.set_password("AGENTLAB", "GOOGLE_API_KEY", api_key)
    load_apikey()

# PARA DELETAR A CHAVE API
def delete_apikey():
    keyring.delete_password("AGENTLAB", "GOOGLE_API_KEY")
