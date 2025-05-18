import json
import os

# CLASSE RESPONSÁVEL POR GERENCIAR CRIAÇÃO, EXCLUSÃO, CARREGAMENTO (SSD/HD), ESCRITA (SSD/HD) E GERENCIAMENTO VIA MEMÓRIA
class Agents:
    def __init__(self):
        self.agents = []
        self.__load_agents()

    # ADICIONAR AGENTE
    def add_agent(self, name:str, model:str, tools:str, instruction:str, description:str=""):
        self.agents.append(
            {
                "name": name,
                "model": model,
                "tools": tools,
                "instruction": instruction,
                "description": description
            }
        )
        self.save_agents()
    
    # DELETAR AGENTE (MEMÓRIA E SSD/HD)
    def delete_agent(self, index: int):
        self.agents.pop(index)
        self.save_agents()

    # SALVAR AGENTE (SSD/HD)
    def save_agents(self):
        with open("./storage/data/agents.json", "w") as file:
            json.dump(self.agents, file, indent=4)

    # CARREGAR DO SSD/HD
    def __load_agents(self):
        if os.path.exists("./storage/data/agents.json"):
            with open("./storage/data/agents.json", "r") as file:
                self.agents = json.load(file)

agents = Agents()