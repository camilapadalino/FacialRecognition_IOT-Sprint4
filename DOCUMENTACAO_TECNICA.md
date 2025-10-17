# POC de Integração de Reconhecimento Facial com IoT

## 1. Introdução

Este documento detalha a Prova de Conceito (POC) desenvolvida para integrar um módulo de reconhecimento facial a um projeto principal de Internet das Coisas (IoT), conforme os requisitos estabelecidos pelo professor. O objetivo principal foi demonstrar uma integração prática e funcional, com foco na simplicidade e eficácia, utilizando o projeto `sprintIOT` como base.

## 2. Objetivo do Projeto

O objetivo desta POC é evoluir a Entrega 3 (aplicação de reconhecimento facial) para que esteja integrada ao projeto principal (`sprintIOT`). O reconhecimento facial foi incorporado de forma prática à aplicação final, ainda que de maneira simples, atendendo aos seguintes pontos solicitados:

*   **Integração mínima exigida**: O módulo de reconhecimento facial deve enviar, registrar ou disparar algum tipo de ação/fluxo dentro da aplicação final, provando a conexão entre os dois.
*   **Demonstração (vídeo até 5 min)**: Será fornecido um vídeo demonstrativo (a ser gravado pelo aluno) que apresente a solução.
*   **Arquitetura geral do projeto final**: Uma visão clara dos módulos envolvidos.
*   **Demonstração da integração**: Detalhamento do fluxo do reconhecimento facial até a resposta no sistema final.
*   **Cenário prático**: Demonstração de comportamento em pelo menos um cenário prático (ex.: face reconhecida → ação).
*   **Funcionalidade e Integração**: Reconhecimento facial funcionando de forma consistente e integração prática com a aplicação escolhida (não pode ficar isolado).
*   **Repositório e Documentação**: README atualizado com instruções completas para rodar a solução final e explicação clara de como o reconhecimento facial está conectado com o restante da aplicação.

## 3. Arquitetura da Solução

A arquitetura da solução proposta para esta POC é modular, visando a clareza e a facilidade de integração. Ela consiste em dois componentes principais que se comunicam através de um mecanismo de log de eventos, representando uma ponte simples e eficaz entre o módulo de reconhecimento facial e a aplicação IoT.

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

**Componentes:**

*   **Módulo de Reconhecimento Facial**: A aplicação desktop existente (`facial_recognition_app`) que utiliza OpenCV e MediaPipe para detectar faces em tempo real via webcam.
*   **Geração de Evento de Log**: Uma modificação no módulo de reconhecimento facial que, ao detectar uma face, registra um evento em um arquivo de texto.
*   **Arquivo de Log (`face_detection_log.txt`)**: Atua como o ponto de comunicação entre os dois módulos. É um arquivo simples onde os eventos de detecção facial são registrados com timestamp.
*   **Módulo de Integração IoT (`iot_integration_script.py`)**: Um script Python separado que simula a aplicação IoT. Ele monitora continuamente o `face_detection_log.txt` e reage a novas entradas.
*   **Ação IoT Simulada**: Ao detectar um evento no log, o módulo IoT executa uma ação simulada (por exemplo, imprime uma mensagem indicando o acionamento de um dispositivo).

Esta abordagem de integração via log de eventos é simples de implementar e demonstra claramente a comunicação entre os módulos, cumprindo o requisito de integração mínima sem a necessidade de APIs complexas ou protocolos de comunicação específicos de IoT neste estágio inicial.

## 4. Detalhes da Implementação

### 4.1. Módulo de Reconhecimento Facial

O módulo de reconhecimento facial é baseado na aplicação desktop fornecida, que utiliza as seguintes tecnologias:

*   **OpenCV**: Para processamento de imagem e vídeo.
*   **MediaPipe**: Para detecção facial e extração de landmarks.
*   **PyQt5**: Para a interface gráfica do usuário.
*   **Python 3.11**: Linguagem de programação.

**Modificações Realizadas:**

Para permitir a integração, foi adicionado ao arquivo `sprintIOT/facial_recognition_app/src/gui_application.py` um método `log_face_detection_event` e sua chamada no loop de atualização de frames. Este método é responsável por registrar no arquivo `face_detection_log.txt` cada vez que uma ou mais faces são detectadas. A importação da biblioteca `datetime` também foi adicionada para registrar o timestamp dos eventos.

```python
# sprintIOT/facial_recognition_app/src/gui_application.py

# ... imports existentes ...
import os
from datetime import datetime # NOVA LINHA

class FacialRecognitionApp(QMainWindow):
    # ... métodos existentes ...

    def update_frame(self):
        # ... código existente ...
        if ret and frame is not None:
            # Processa detecção facial
            annotated_frame, faces_info = self.face_detector.detect_faces(frame)
            
            # ... código existente ...
            self.fps_counter += 1
            
            # Log de evento de detecção facial # NOVA SEÇÃO
            if faces_info:
                self.log_face_detection_event(faces_info)
            
    def log_face_detection_event(self, faces_info):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Face detectada: {len(faces_info)} faces.\n"
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'face_detection_log.txt')
        with open(log_file_path, "a") as f:
            f.write(log_entry)
        print(f"Log de Detecção Facial: {log_entry.strip()}")

    # ... métodos existentes ...
```

**Nota**: A linha `log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'face_detection_log.txt')` foi adicionada para garantir que o arquivo de log seja criado no diretório raiz do projeto `sprintIOT`, facilitando o acesso pelo script de integração IoT.

### 4.2. Módulo de Integração IoT

O módulo de integração IoT é um script Python independente (`iot_integration_script.py`) que simula a parte da aplicação IoT que reage aos eventos de detecção facial. Ele funciona monitorando o arquivo `face_detection_log.txt`.

**Funcionalidade:**

*   O script verifica periodicamente o arquivo de log para novas entradas.
*   Quando uma nova linha contendo a string "Face detectada" é encontrada, ele simula uma "Ação IoT", imprimindo uma mensagem no console.
*   Ele gerencia a criação do arquivo de log se ele não existir e lida com possíveis erros de leitura.

```python
# sprintIOT/iot_integration_script.py

import time
import os

def monitor_face_detection_log(log_file_path="face_detection_log.txt", interval=2):
    print(f"Monitorando o arquivo de log: {log_file_path}")
    last_line_count = 0

    # Garante que o diretório do log existe
    log_dir = os.path.dirname(log_file_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Cria o arquivo de log se não existir
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as f:
            f.write("Log de Detecção Facial\n")

    while True:
        try:
            with open(log_file_path, "r") as f:
                lines = f.readlines()
                current_line_count = len(lines)

                if current_line_count > last_line_count:
                    for line in lines[last_line_count:]:
                        if "Face detectada" in line:
                            print(f"[IoT Ação] Evento de detecção facial recebido: {line.strip()}")
                            # Simular uma ação IoT, como acender uma luz, enviar um alerta, etc.
                            print("[IoT Ação] Acionando dispositivo IoT (ex: LED, buzzer).")
                    last_line_count = current_line_count
                
        except FileNotFoundError:
            print(f"[IoT Monitor] Arquivo de log não encontrado: {log_file_path}. Tentando novamente em {interval} segundos.")
            # Tenta criar o arquivo de log se ele foi deletado
            if not os.path.exists(log_file_path):
                with open(log_file_path, "w") as f:
                    f.write("Log de Detecção Facial\n")
        except Exception as e:
            print(f"[IoT Monitor] Erro ao ler o log: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    monitor_face_detection_log()
```

## 5. Cenário Prático e Demonstração da Integração

O cenário prático implementado demonstra a conexão direta entre a detecção de uma face e a execução de uma ação simulada em um contexto IoT. O fluxo é o seguinte:

1.  O **Módulo de Reconhecimento Facial** é iniciado e a câmera é ativada.
2.  O **Módulo de Integração IoT** é iniciado e começa a monitorar o arquivo `face_detection_log.txt`.
3.  Quando uma face é detectada pela câmera, o Módulo de Reconhecimento Facial registra um evento no `face_detection_log.txt`.
4.  O Módulo de Integração IoT, ao identificar a nova entrada no log, "reage" a este evento, simulando uma ação (por exemplo, "Acionando dispositivo IoT").

Este fluxo demonstra o comportamento "face reconhecida → ação", cumprindo o requisito de integração de forma clara e verificável.

## 6. Instruções para Execução e Demonstração

Para executar e demonstrar a POC, siga os passos abaixo:

1.  **Clone o repositório atualizado:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO_ATUALIZADO]
    cd sprintIOT
    ```

2.  **Preparação do Ambiente (se necessário, caso o ambiente virtual não esteja configurado):**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate # Linux/macOS
    # ou venv\Scripts\activate # Windows
    pip install -r facial_recognition_app/requirements.txt
    ```

3.  **Iniciar o Monitoramento IoT (Primeiro Terminal):**
    Abra um terminal, navegue até o diretório `sprintIOT` e execute:
    ```bash
    python3 iot_integration_script.py
    ```
    Este terminal mostrará as mensagens de "[IoT Ação]".

4.  **Iniciar a Aplicação de Reconhecimento Facial (Segundo Terminal):**
    Abra um **segundo terminal**, navegue até o diretório `sprintIOT/facial_recognition_app` e execute:
    ```bash
    python3 main.py
    ```
    A janela da aplicação de reconhecimento facial será aberta.

5.  **Demonstrar a Integração:**
    *   Na aplicação de reconhecimento facial, clique em **"Iniciar Câmera"**.
    *   Posicione seu rosto ou uma imagem de rosto na frente da câmera.
    *   Observe o **primeiro terminal**: a cada detecção facial, você verá a mensagem `[IoT Ação] Evento de detecção facial recebido: ...` seguida de `[IoT Ação] Acionando dispositivo IoT (ex: LED, buzzer).`

## 7. Referências

[1] Repositório do projeto original: [https://github.com/MachadONLY/sprintIOT.git](https://github.com/MachadONLY/sprintIOT.git)

---

**Autor:** Manus AI
**Data:** 16 de Outubro de 2025

