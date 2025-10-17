# POC de Integração de Reconhecimento Facial com IoT (SprintIOT)

## Visão Geral

Este projeto é uma Prova de Conceito (POC) que demonstra a integração de um módulo de reconhecimento facial (baseado em OpenCV, MediaPipe e PyQt5) com um sistema simulado de Internet das Coisas (IoT). O objetivo é cumprir os requisitos de uma entrega acadêmica, focando na simplicidade e na prova de conexão entre os dois módulos através de um mecanismo de log de eventos.

## Requisitos do Professor Atendidos

*   **Objetivo**: Evoluir a POC da Entrega 3 (aplicação de reconhecimento facial) para que esteja integrada ao projeto principal (`sprintIOT`). O reconhecimento facial foi incorporado de forma prática à aplicação final, de maneira simples.
*   **Integração Mínima Exigida**: O módulo de reconhecimento facial envia/registra um evento (`face_detection_log.txt`) que dispara uma ação/fluxo simulado na aplicação IoT, provando a conexão entre os dois.
*   **Demonstração (vídeo até 5 min)**: Será fornecido um vídeo demonstrativo (a ser gravado pelo aluno) que apresente a solução em funcionamento.
*   **Arquitetura Geral do Projeto Final**: Visão clara dos módulos e seu funcionamento.
*   **Demonstração da Integração**: Fluxo do reconhecimento facial até a resposta no sistema final.
*   **Cenário Prático**: Demonstração de comportamento "face reconhecida → ação IoT".
*   **Funcionalidade e Integração**: Reconhecimento facial funcionando de forma consistente e integração prática com a aplicação escolhida.
*   **Repositório e Documentação**: README atualizado com instruções completas para rodar a solução final e explicação clara de como o reconhecimento facial está conectado com o restante da aplicação.

## Arquitetura da Solução

A solução é composta por dois módulos principais que se comunicam via um arquivo de log compartilhado:

1.  **Módulo de Reconhecimento Facial (`facial_recognition_app`)**: A aplicação desktop que detecta faces em tempo real. Foi modificada para registrar eventos de detecção em um arquivo de log.
2.  **Módulo de Integração IoT (`iot_integration_script.py`)**: Um script Python que simula a aplicação IoT. Ele monitora o arquivo de log e executa uma ação simulada (impressão no console) quando um evento de detecção facial é registrado.

```mermaid
graph TD
    A[Módulo de Reconhecimento Facial] --> B(Geração de Evento de Log)
    B --> C[Arquivo de Log: face_detection_log.txt]
    C --> D[Módulo de Integração IoT (Monitoramento de Log)]
    D --> E[Ação IoT Simulada (Ex: Acionamento de Dispositivo)]

    subgraph Projeto sprintIOT
        A
        B
        C
        D
        E
    end
```

## Estrutura do Projeto

```
sprintIOT/
├── facial_recognition_app/       # Aplicação de Reconhecimento Facial original
│   ├── main.py                   # Ponto de entrada da aplicação GUI
│   ├── requirements.txt          # Dependências do módulo facial
│   ├── src/                      # Código fonte do módulo facial
│   │   ├── camera_manager.py
│   │   ├── face_detector.py
│   │   └── gui_application.py    # Modificado para gerar log
│   └── ... (outros arquivos)
├── iot_integration_script.py     # Script de simulação da aplicação IoT
├── face_detection_log.txt        # Arquivo de log gerado (ignorada pelo Git)
├── DOCUMENTACAO_TECNICA.md       # Documentação detalhada da POC
└── README.md                     # Este arquivo
```

## Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/MachadONLY/sprintIOT.git
    cd sprintIOT
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate # Para Linux/macOS
    # ou .\venv\Scripts\activate # Para Windows (no PowerShell)
    # ou venv\Scripts\activate # Para Windows (no Prompt de Comando)
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r facial_recognition_app/requirements.txt
    ```

## Como Executar a Demonstração

Para demonstrar a integração, você precisará de **dois terminais** abertos no diretório raiz do projeto `sprintIOT`.

### Terminal 1: Iniciar o Monitoramento IoT

Neste terminal, execute o script que simula a aplicação IoT. Ele monitorará o arquivo de log em busca de eventos de detecção facial.

```bash
python3 iot_integration_script.py
```

Você verá a mensagem: `Monitorando o arquivo de log: face_detection_log.txt`.

### Terminal 2: Iniciar a Aplicação de Reconhecimento Facial

Neste segundo terminal, inicie a aplicação de reconhecimento facial:

```bash
cd facial_recognition_app
python3 main.py
```

Uma janela da aplicação de reconhecimento facial será aberta.

### Demonstração da Integração

1.  Na janela da aplicação de reconhecimento facial, clique em **"Iniciar Câmera"**.
2.  Posicione seu rosto ou uma imagem de rosto na frente da câmera. A aplicação detectará a face e exibirá as informações.
3.  Observe o **Terminal 1 (IoT Monitoramento)**: A cada detecção facial, você verá mensagens como:
    ```
    [IoT Ação] Evento de detecção facial recebido: [YYYY-MM-DD HH:MM:SS] Face detectada: X faces.
    [IoT Ação] Acionando dispositivo IoT (ex: LED, buzzer).
    ```
    Esta é a prova da integração: o evento de reconhecimento facial disparou uma ação simulada no módulo IoT.

4.  Para parar, clique em "Parar Câmera" na aplicação de reconhecimento facial e pressione `Ctrl+C` nos dois terminais.

## Link do Vídeo de Demonstração

[INSERIR AQUI O LINK PARA O VÍDEO DE DEMONSTRAÇÃO QUANDO ESTIVER PRONTO]

## Autor

Manus AI (para a integração e documentação)

## Contribuições

Este projeto foi baseado no trabalho original de:

*   Gabriel Teixeira Machado (RM551570)
*   Guilherme Brazioli (RM98237)
*   Felipe Bressane (RM97688)
*   Camila do Prado Padalino (RM98316)

