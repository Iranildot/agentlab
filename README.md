# AgentLab - Plataforma para Desenvolvimento e Experimentação de Agentes (Google Gemini)

![Licença](https://img.shields.io/badge/licence-MIT-blue.svg)
![Contribuições](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Issues Abertas](https://img.shields.io/github/issues/Iranildot/agentlab)
![Código de Conduta](https://img.shields.io/badge/code%20of%20conduct-enforced-brightgreen)

AgentLab é um aplicativo intuitivo projetado para facilitar a criação e otimização de agentes autônomos, utilizando a API do Google Gemini para acesso a modelos LLM (Large Language Models). Ele oferece um ambiente completo para automação de tarefas, experimentação e testes, permitindo o desenvolvimento ágil e eficiente de agentes inteligentes.


---

## 🔍 Visão Geral

Este repositório contém o código-fonte, documentação e exemplos da plataforma AgentLab. Ele foi criado para ser:

- **Fácil de usar**
- **Voltado a pesquisadores, desenvolvedores e estudantes**

---

## ✨ Funcionalidades Principais

- **Ambiente de teste integrado**: Permite ao usuário visualizar e avaliar o comportamento dos agentes em tempo real, garantindo maior controle e precisão nos ajustes.
- **Criação manual de agentes**: Oferece total flexibilidade ao usuário para definir manualmente as configurações de cada agente, incluindo modelo LLM, instruções e ferramentas.
- **Criação automática de agentes**: Um agente especializado gera automaticamente novos agentes com base em um prompt fornecido pelo usuário, agilizando o processo de criação.
- **Configuração de temas**: O usuário pode alternar entre diferentes temas visuais para adaptar a interface às suas preferências estéticas ou de acessibilidade.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento da plataforma.

- **Google Generative AI (`google.generativeai`)**: Interface com os modelos LLM da Google (como Gemini), que compõem o núcleo de raciocínio dos agentes.

- **Flet**: Framework para construção da interface gráfica de forma rápida e responsiva, utilizando Python puro.

- **Keyring**: Biblioteca utilizada para gerenciamento seguro de credenciais e chaves de API no sistema.

- **JSON**: Utilizado para a estruturação, leitura e escrita dos dados de configuração dos agentes.

- **Agents (`google.adk.agents`)** *(ou outro framework de agentes)*: Planejado para orquestração e execução de agentes autônomos. Pode ser substituído futuramente por frameworks como JADE, SPADE ou uma solução personalizada.

- **Outras dependências**: Listadas no arquivo [`requirements.txt`](requirements.txt), incluindo bibliotecas auxiliares para testes, simulação e integração.


---

## 📦 Requisitos

- Python 3.x
- Pip
- As dependências listadas no `requirements.txt`

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/Iranildot/agentlab.git
cd agentlab

# (Opcional) Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Aparência do aplicativo

### Área de prompt

![Captura de tela de 2025-05-17 22-22-59](https://github.com/user-attachments/assets/318a3705-7288-45a2-9248-dbeafb2fb7a9)

---

### Área de agentes


![Captura de tela de 2025-05-17 22-23-17](https://github.com/user-attachments/assets/6dbcb6fc-59b3-44ab-91d7-eccc781fa2cd)

---

### Modo escuro

![Captura de tela de 2025-05-17 22-23-43](https://github.com/user-attachments/assets/8a6901a3-29ae-43e8-97ec-8d090bbd190a)
