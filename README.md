# 🧠💡 POC de Integração de Reconhecimento Facial com IoT e MoneyWise App
### *Projeto Acadêmico — Sprint 4 - IoT — FIAP 2025*

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange?logo=opencv)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey)
![React Native](https://img.shields.io/badge/React_Native-App-blueviolet?logo=react)
![Status](https://img.shields.io/badge/Status-POC%20Completa-brightgreen)
![License](https://img.shields.io/badge/License-Acad%C3%AAmico-lightgrey)

---

## 🚀 Alunos:
- Camila do Prado Padalino - RM98316
- Felipe Cavalcante Bressane - RM97688
- Gabriel Teixeira Machado - RM551570
- Guilherme Brazioli - RM98237

---

## 🎬 Vídeo de Demonstração

### 📺 https://drive.google.com/file/d/1jf9xGbGNvSGTHyuX2_VFu4YbV4XBv-nx/view?usp=sharing

---

## 📘 Visão Geral

Esta **Prova de Conceito (POC)** demonstra a integração entre um sistema de **reconhecimento facial** (usando *OpenCV*, *MediaPipe* e *Python com Flask*) e o **MoneyWise App**, um aplicativo mobile desenvolvido em *React Native (Expo)*.

O foco é **provar a comunicação entre os módulos** — quando uma face é detectada pela API Python, o `MoneyWise App` consulta essa API e reage, simulando ações como autenticação ou registro de eventos. Esta abordagem cumpre o requisito de integração de forma prática e escalável.

---

## 🔮 Integração com o MoneyWise App

Esta POC serve como **base tecnológica** para a integração do reconhecimento facial no aplicativo [**MoneyWise App**](https://github.com/camilapadalino/MoneyWiseApp), um projeto desenvolvido anteriormente pela equipe e voltado à **educação financeira com apoio de inteligência artificial (IA)**.

A implementação do **reconhecimento facial** no *MoneyWise App* agrega **segurança, personalização e análise comportamental** à experiência do usuário.

### 📌 Aplicações no MoneyWise App

-   **🔐 Autenticação e Login Inteligente:**
    Permitir que os usuários acessem o aplicativo ou confirmem transações financeiras utilizando o reconhecimento facial como método de autenticação biométrica.
    Essa integração proporciona **maior segurança e praticidade**, eliminando a necessidade de senhas convencionais e reduzindo riscos de acesso indevido.

-   **🧾 Registro de Presença e Auditoria de Sessões:**
    Utilizar o reconhecimento facial para **registrar a presença e as atividades** dos usuários, criando um **histórico seguro de acessos**.
    Esse registro poderá ser utilizado para **auditoria, monitoramento de segurança** e análise de padrões de uso dentro do aplicativo.

-   **📊 Dados para Dashboards e Business Intelligence (BI):**
    Integrar os dados provenientes do reconhecimento facial ao **painel de BI do MoneyWise**, permitindo **análises avançadas de comportamento**, identificação de padrões e geração de **insights estratégicos** sobre a utilização do aplicativo.

### 💡 Objetivo da Integração

O objetivo dessa integração é **expandir o ecossistema do MoneyWise App**, incorporando tecnologias de **visão computacional e biometria facial**. Essa evolução reforça o compromisso do projeto com a **inovação, segurança e experiência do usuário**, utilizando a POC atual como **prova de viabilidade técnica** da comunicação entre módulos de reconhecimento facial e sistemas de gestão financeira inteligentes.

---

## 🧠 Tecnologias Utilizadas:
-   **Categoria:**	Ferramentas / Bibliotecas <br>
-   **Linguagem:**	Python 3.11, JavaScript (React Native) <br>
-   **Visão Computacional:**	OpenCV, MediaPipe <br>
-   **API:**	Flask, Flask-CORS <br>
-   **Interface Gráfica (App):**	React Native (Expo) <br>
-   **Ambiente:**	Cross-platform (Windows/Linux/macOS para API, Android/iOS para App)

---

## ⚙️ Instalação e Configuração

### 1. Clone os Repositórios

Clone ambos os repositórios para o seu computador:

```bash
# Repositório da POC de Reconhecimento Facial (este repositório)
git clone https://github.com/camilapadalino/FacialRecognition_IOT-Sprint4.git
cd FacialRecognition_IOT-Sprint4

# Repositório do MoneyWise App
git clone https://github.com/camilapadalino/MoneyWiseApp.git
```

### 2. Configuração do Ambiente Python (API de Reconhecimento Facial)

Navegue até a pasta `FacialRecognition_IOT-Sprint4` no seu terminal:

```bash
cd FacialRecognition_IOT-Sprint4
```

Crie e ative um ambiente virtual (venv):

```bash
python3.11 -m venv venv
# Para Windows PowerShell:
.\venv\Scripts\activate
# Para Linux/macOS:
source venv/bin/activate
```

Instale as dependências da API:

```bash
pip install -r facial_recognition_app/requirements.txt
```

### 3. Configuração do Ambiente React Native (MoneyWise App)

Navegue até a pasta `MoneyWiseApp` no seu terminal:

```bash
cd ../MoneyWiseApp
```

Instale as dependências do aplicativo:

```bash
npm install
# Se necessário, instale dependências adicionais do Firebase/Navegação:
npm install firebase @react-native-async-storage/async-storage @react-navigation/native @react-navigation/native-stack @react-navigation/bottom-tabs
```

**Atenção:** Você precisará ter o Node.js e o npm/npx instalados no seu sistema. Se não tiver, baixe a versão LTS em [https://nodejs.org/en](https://nodejs.org/en).

### 4. Configure o IP da API no MoneyWise App

Para que o MoneyWise App se conecte à API de reconhecimento facial, você precisa informar o endereço IP do seu computador.

1.  **Encontre o Endereço IP do seu Computador:**
    *   Abra o **Prompt de Comando** (CMD) no Windows.
    *   Digite `ipconfig` e aperte Enter.
    *   Procure por **"Endereço IPv4"** do seu adaptador de rede principal (geralmente Ethernet ou Wi-Fi). Anote o número (ex: `192.168.15.168`).
    *   **Importante:** O IP que a API Flask exibe ao iniciar (ex: `http://192.168.15.168:5000`) é o que você deve usar.

2.  **Edite o arquivo `MoneyWiseApp/screens/FacialRecognition.js`:**
    *   Abra este arquivo no seu editor de código.
    *   Localize a linha que define `API_URL` (aproximadamente linha 19):
        ```javascript
        const API_URL = 'http://localhost:5000/api'; // OU 'http://192.168.X.X:5000/api';
        ```
    *   Substitua `localhost` (ou o IP antigo) pelo **endereço IP do seu computador** que você encontrou (ex: `192.168.15.168`). A linha deve ficar assim:
        ```javascript
        const API_URL = 'http://192.168.15.168:5000/api';
        ```
    *   Salve o arquivo.

---

## 🚀 Como Executar a Demonstração

> 🧠 **Dica:** Mantenha o seu computador e o celular/emulador na **MESMA REDE Wi-Fi** para que a comunicação funcione.

### 🖥️ Terminal 1 — Iniciar a API de Reconhecimento Facial

Abra um terminal, navegue até a pasta `FacialRecognition_IOT-Sprint4`, ative o ambiente virtual e execute a API:

```bash
cd FacialRecognition_IOT-Sprint4
.\venv\Scripts\activate # ou source venv/bin/activate
python facial_recognition_app/api_server.py
```

Este terminal mostrará que a API foi iniciada e estará "ouvindo" na porta `5000`. **Deixe este terminal aberto e rodando.**

### 📱 Terminal 2 — Iniciar o MoneyWise App

Abra um **segundo terminal**, navegue até a pasta `MoneyWiseApp` e inicie o aplicativo Expo:

```bash
cd MoneyWiseApp
npx expo start
```

Um QR Code será exibido. Escaneie-o com o aplicativo **Expo Go** no seu celular ou abra em um emulador.

### 🔄 Fluxo de Integração em Tempo Real

1.  No **MoneyWise App**, navegue até a tela **"🔐 Facial"** (na barra de navegação inferior).
2.  Verifique o **"Status da API"**. Ele deve mostrar **"🟢 Conectado"**.
3.  Clique no botão **"▶️ Iniciar Detecção"** no aplicativo.
4.  Posicione seu rosto (ou uma imagem de rosto) na frente da **câmera do seu computador**.
    *   A luz da sua câmera deve acender, indicando que a API está acessando-a.
    *   O aplicativo no celular/emulador mostrará **"✅ Face Detectada!"** e a contagem de faces.
5.  Remova seu rosto da câmera. O status no aplicativo deve mudar para "Nenhuma face detectada".
6.  Clique em **"⏹️ Parar Detecção"** no aplicativo para finalizar.

### 🧩 Prova da Integração:

A detecção facial realizada pela API Python é comunicada em tempo real ao MoneyWise App, demonstrando uma integração funcional e prática entre os módulos.

Para encerrar:

Pressione `Ctrl+C` em ambos os terminais.

---

## 7. Referências

[1] Repositório da POC de Reconhecimento Facial: [https://github.com/camilapadalino/FacialRecognition_IOT-Sprint4.git](https://github.com/camilapadalino/FacialRecognition_IOT-Sprint4.git)
[2] Repositório do MoneyWise App: [https://github.com/camilapadalino/MoneyWiseApp.git](https://github.com/camilapadalino/MoneyWiseApp.git)
