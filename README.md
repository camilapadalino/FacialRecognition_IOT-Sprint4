# 🧠💡 POC de Integração de Reconhecimento Facial com IoT  
### *Projeto Acadêmico — Sprint 4 - IoT — FIAP 2025*

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange?logo=opencv)
![IoT](https://img.shields.io/badge/IoT-Simulation-success)
![Status](https://img.shields.io/badge/Status-POC%20Completa-brightgreen)
![License](https://img.shields.io/badge/License-Acad%C3%AAmico-lightgrey)

---

## 🚀 Alunos:
- Camila do Prado Padalino - RM98316
- Felipe Cavalcante Bressane - RM97688
- Gabriel Teixeira Machado - RM551570
- Guilherme Brazioli - RM98237

---

## 📘 Visão Geral

Esta **Prova de Conceito (POC)** demonstra a integração entre um sistema de **reconhecimento facial** (usando *OpenCV*, *MediaPipe* e *PyQt5*) e uma **simulação de aplicação IoT**, atendendo aos requisitos de entrega acadêmica.

O foco é **provar a comunicação entre os módulos** — quando uma face é detectada, um evento é registrado e o módulo IoT simula uma ação (por exemplo, acionar um dispositivo).

---

## 🔮 Integração Futura com o MoneyWise App

Esta POC serve como **base tecnológica** para futuras integrações com o aplicativo [**MoneyWise App**](https://github.com/camilapadalino/MoneyWiseApp), um projeto desenvolvido anteriormente pela equipe e voltado à **educação financeira com apoio de inteligência artificial (IA)**.

A implementação do **reconhecimento facial** no *MoneyWise App* está planejada para as próximas etapas de desenvolvimento e deverá agregar **segurança, personalização e análise comportamental** à experiência do usuário.

---

### 📌 Aplicações Futuras no MoneyWise App

- **🔐 Autenticação e Login Inteligente:**  
  Permitir que os usuários acessem o aplicativo ou confirmem transações financeiras utilizando o reconhecimento facial como método de autenticação biométrica.  
  Essa integração proporcionará **maior segurança e praticidade**, eliminando a necessidade de senhas convencionais e reduzindo riscos de acesso indevido.

- **🧾 Registro de Presença e Auditoria de Sessões:**  
  Utilizar o reconhecimento facial para **registrar a presença e as atividades** dos usuários, criando um **histórico seguro de acessos**.  
  Esse registro poderá ser utilizado para **auditoria, monitoramento de segurança** e análise de padrões de uso dentro do aplicativo.

- **📊 Dados para Dashboards e Business Intelligence (BI):**  
  Integrar os dados provenientes do reconhecimento facial ao **painel de BI do MoneyWise**, permitindo **análises avançadas de comportamento**, identificação de padrões e geração de **insights estratégicos** sobre a utilização do aplicativo.

---

### 💡 Objetivo da Integração

O objetivo dessa integração é **expandir o ecossistema do MoneyWise App**, incorporando tecnologias de **visão computacional e biometria facial**.  
Essa evolução reforça o compromisso do projeto com a **inovação, segurança e experiência do usuário**, utilizando a POC atual como **prova de viabilidade técnica** da comunicação entre módulos de reconhecimento facial e sistemas de gestão financeira inteligentes.

---

## 🎬 Vídeo de Demonstração

### 📺 [Inserir link aqui quando disponível]

---
## 🧠 Tecnologias Utilizadas:
- **Categoria:**	Ferramentas / Bibliotecas <br>
- **Linguagem:**	Python 3.11 <br>
- **Visão Computacional:**	OpenCV, MediaPipe <br>
- **Interface Gráfica:**	PyQt5 <br>
- **Integração IoT:**	Monitoramento de arquivos (os, time) <br>
- **Ambiente:**	Cross-platform (Windows/Linux/macOS)

--- 

## ⚙️ Instalação e Configuração
### 1. Clone o repositório
```bash
git clone https://github.com/camilapadalino/FacialRecognition_IOT-Sprint4.git
cd FacialRecognition_IOT-Sprint4
```
### 2. Crie e ative um ambiente virtual
```bash
python3.11 -m venv venv
source venv/bin/activate          # Linux/macOS
# ou
.\venv\Scripts\activate           # Windows PowerShell
```
### 3. Instale as dependências
``` bash
pip install -r facial_recognition_app/requirements.txt
```
---

## 🚀 Como Executar a Demonstração

> 🧠 Dica: abra dois terminais no diretório raiz sprintIOT.

### 🖥️ Terminal 1 — Iniciar o Monitoramento IoT

Executa o script que simula o sistema IoT, monitorando eventos do log.
````
python3 iot_integration_script.py
````
Saída esperada:

> Monitorando o arquivo de log: face_detection_log.txt


### 🎥 Terminal 2 — Iniciar a Aplicação de Reconhecimento Facial

Execute a aplicação GUI do módulo facial:
````
cd facial_recognition_app
python3 main.py
````
A janela será aberta com os controles de câmera e detecção facial.

### 🔄 Fluxo de Integração em Tempo Real

1. Clique em “Iniciar Câmera”.

2. Aponte seu rosto ou uma imagem com rostos.

A aplicação detectará a(s) face(s) e registrará o evento no log.

Observe o Terminal 1 — o módulo IoT exibirá mensagens como:
````
[IoT Ação] Evento de detecção facial recebido: [2025-10-17 15:45:22]
[IoT Ação] Acionando dispositivo IoT (ex: LED, buzzer)
````

### 🧩 Prova da integração: a detecção facial gera um evento que aciona uma resposta IoT simulada.

Para encerrar:

Clique em “Parar Câmera” na GUI.

Pressione Ctrl+C em ambos os terminais.
