# Aplicação de Reconhecimento Facial - IOT & JOB

Uma aplicação desktop para reconhecimento e identificação facial em tempo real usando OpenCV, MediaPipe e PyQt5.

Gabriel teixeira machado rm551570 Guilherme Brazioli rm98237 Felipe Bressane rm97688 Camila do Prado Padalino rm98316

## 📋 Objetivo

Desenvolver uma aplicação local (desktop/notebook) que realize reconhecimento/identificação facial do usuário usando OpenCV, IA/ML ou Haar Cascade (qualquer tecnologia que envolva parâmetros ajustáveis). A aplicação não precisa estar conectada à aplicação/solução final.

## 🚀 Características Principais

- **Detecção facial em tempo real** usando MediaPipe
- **Landmarks faciais** com visualização detalhada dos pontos característicos
- **Interface gráfica intuitiva** desenvolvida em PyQt5
- **Parâmetros ajustáveis** em tempo real para demonstração de impacto
- **Identificação facial simplificada** usando comparação de histogramas
- **Estatísticas em tempo real** (FPS, número de faces detectadas)
- **Código executável** com instruções claras

## 🛠️ Tecnologias Utilizadas

- **OpenCV 4.12.0**: Processamento de imagem e vídeo
- **MediaPipe 0.10.14**: Detecção facial e landmarks
- **PyQt5**: Interface gráfica
- **NumPy**: Operações matemáticas e arrays
- **Python 3.11**: Linguagem de programação

## 📦 Requisitos do Sistema

- Python 3.11 ou superior
- Câmera web (opcional, para demonstração em tempo real)
- Sistema operacional: Windows, macOS ou Linux
- Memória RAM: Mínimo 4GB recomendado
- Processador: Qualquer processador moderno (x86_64)

## 🔧 Instalação e Configuração

### 1. Preparação do Ambiente

```bash
# Clone ou extraia o projeto
cd facial_recognition_app

# Crie um ambiente virtual Python
python3.11 -m venv venv

# Ative o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows:
# venv\\Scripts\\activate
```

### 2. Instalação das Dependências

```bash
# Instale as dependências necessárias
pip install opencv-python mediapipe PyQt5
```

### 3. Verificação da Instalação

```bash
# Execute o script de teste
python test_app.py
```

Se todos os testes passarem, a aplicação está pronta para uso.

## 🎮 Como Executar

### Execução Principal

```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate  # Linux/macOS
# ou
# venv\\Scripts\\activate  # Windows

# Execute a aplicação
python main.py
```

### Execução Alternativa

```bash
# Execução direta do módulo principal
python src/gui_application.py
```

## 📱 Como Usar a Aplicação

### Interface Principal

A aplicação possui uma interface dividida em três seções principais:

1. **Painel de Vídeo (Esquerda)**:
   - Exibe o feed da câmera em tempo real
   - Mostra as detecções faciais com anotações
   - Botões para iniciar/parar a câmera

2. **Painel de Parâmetros (Direita Superior)**:
   - **Confiança de Detecção**: Ajusta a sensibilidade da detecção facial (0.10 - 1.00)
   - **Confiança de Rastreamento**: Ajusta a estabilidade do rastreamento (0.10 - 1.00)
   - **Opções de Visualização**:
     - Mostrar Landmarks Faciais
     - Mostrar Caixas Delimitadoras
     - Mostrar ID das Faces

3. **Painel de Informações (Direita Inferior)**:
   - Informações detalhadas das faces detectadas
   - Estatísticas em tempo real (FPS, contagem de faces)

### Controles e Parâmetros

#### Parâmetros Ajustáveis

1. **Confiança de Detecção (0.10 - 1.00)**:
   - **Valores baixos (0.10-0.40)**: Detecta mais faces, mas pode gerar falsos positivos
   - **Valores médios (0.50-0.70)**: Balanceamento entre precisão e recall
   - **Valores altos (0.80-1.00)**: Detecta apenas faces com alta confiança

2. **Confiança de Rastreamento (0.10 - 1.00)**:
   - **Valores baixos**: Rastreamento mais sensível a mudanças
   - **Valores altos**: Rastreamento mais estável, menos oscilação

#### Opções de Visualização

- **Landmarks Faciais**: Exibe pontos característicos do rosto (olhos, nariz, boca, contorno)
- **Caixas Delimitadoras**: Mostra retângulos ao redor das faces detectadas
- **ID das Faces**: Exibe identificadores únicos para cada face

### Demonstração de Impacto dos Parâmetros

Para demonstrar o impacto dos parâmetros:

1. **Inicie a aplicação** e ative a câmera
2. **Ajuste a confiança de detecção**:
   - Diminua para 0.20 e observe mais detecções (possivelmente falsas)
   - Aumente para 0.80 e observe detecções mais conservadoras
3. **Teste as opções de visualização**:
   - Desative landmarks para ver apenas as caixas
   - Ative/desative diferentes combinações
4. **Observe as estatísticas** em tempo real no painel de informações

## 🏗️ Estrutura do Projeto

```
facial_recognition_app/
├── main.py                 # Arquivo principal de execução
├── test_app.py            # Script de testes
├── README.md              # Documentação (este arquivo)
├── requirements.txt       # Dependências do projeto
└── src/                   # Código fonte
    ├── face_detector.py   # Módulo de detecção facial
    ├── camera_manager.py  # Gerenciamento da câmera
    └── gui_application.py # Interface gráfica principal
```

### Descrição dos Módulos

#### `face_detector.py`
- Classe `FaceDetector`: Implementa detecção facial usando MediaPipe
- Métodos para detecção, landmarks e identificação facial
- Parâmetros ajustáveis em tempo real
- Comparação de faces usando histogramas

#### `camera_manager.py`
- Classe `CameraManager`: Gerencia captura de vídeo
- Configuração de resolução e propriedades da câmera
- Tratamento de erros e liberação de recursos

#### `gui_application.py`
- Interface gráfica principal usando PyQt5
- Painéis de controle e visualização
- Integração entre detector facial e câmera
- Atualização em tempo real dos parâmetros

## 🔍 Funcionalidades Técnicas

### Detecção Facial
- Utiliza o modelo de detecção facial do MediaPipe
- Suporte para múltiplas faces simultâneas (até 5)
- Detecção de landmarks faciais com 468 pontos
- Cálculo de confiança para cada detecção

### Identificação Facial
- Implementação simplificada usando histogramas de intensidade
- Comparação de faces baseada em correlação
- Extração de características da região facial
- Normalização e redimensionamento automático

### Interface e Usabilidade
- Interface responsiva e intuitiva
- Controles em tempo real sem necessidade de reinicialização
- Feedback visual imediato das alterações
- Estatísticas de performance (FPS)

## 🧪 Testes e Validação

### Script de Testes Automatizados

Execute `python test_app.py` para validar:

- ✅ Importação de todas as dependências
- ✅ Criação e configuração do detector facial
- ✅ Funcionamento do gerenciador de câmera
- ✅ Atualização de parâmetros em tempo real
- ✅ Liberação adequada de recursos

### Cenários de Teste Manual

1. **Teste sem câmera**: A aplicação deve iniciar normalmente e exibir mensagem apropriada
2. **Teste com câmera**: Detecção facial deve funcionar em tempo real
3. **Teste de parâmetros**: Alterações devem refletir imediatamente na detecção
4. **Teste de performance**: FPS deve ser estável (>15 FPS em hardware moderno)

## ⚠️ Limitações e Próximos Passos

### Limitações Atuais

- **Identificação facial**: Implementação simplificada usando histogramas (não é robusta para identificação real)
- **Dependência de iluminação**: Performance pode variar com condições de luz
- **Processamento single-thread**: Não otimizado para múltiplos cores
- **Armazenamento**: Não salva faces ou dados de identificação

### Próximos Passos

- Implementar identificação facial mais robusta (ex: usando embeddings faciais)
- Adicionar suporte para salvar e carregar perfis de faces
- Otimizar performance para processamento em tempo real
- Adicionar mais opções de visualização e análise
- Implementar detecção de emoções e características faciais

## 🔒 Considerações Éticas e Privacidade

### Uso Responsável de Dados Faciais

Esta aplicação foi desenvolvida para fins educacionais e de demonstração. Ao usar tecnologias de reconhecimento facial, é importante considerar:

#### Privacidade e Consentimento
- **Sempre obtenha consentimento** antes de processar dados biométricos de terceiros
- **Não armazene** dados faciais sem autorização explícita
- **Informe claramente** sobre o processamento de dados biométricos

#### Segurança dos Dados
- **Processamento local**: Esta aplicação processa dados localmente, sem envio para servidores externos
- **Não persistência**: Os dados faciais não são salvos permanentemente
- **Acesso limitado**: Apenas a aplicação tem acesso aos dados durante a execução

#### Conformidade Legal
- **LGPD (Brasil)**: Dados biométricos são considerados sensíveis
- **GDPR (Europa)**: Requer consentimento explícito para processamento
- **Outras jurisdições**: Verifique as leis locais aplicáveis

#### Recomendações de Uso
- Use apenas para fins educacionais, pesquisa ou desenvolvimento
- Não implemente em produção sem revisão legal adequada
- Considere implementar controles de acesso e auditoria
- Documente claramente o propósito e escopo do processamento

### Responsabilidade do Desenvolvedor

O desenvolvedor desta aplicação não se responsabiliza pelo uso inadequado ou ilegal da tecnologia. É responsabilidade do usuário garantir conformidade com leis e regulamentações aplicáveis.

## 📞 Suporte e Contribuições

### Problemas Conhecidos

- **Erro de câmera**: Se a câmera não iniciar, verifique se não está sendo usada por outro aplicativo
- **Performance baixa**: Em hardware mais antigo, reduza a resolução da câmera
- **Dependências**: Certifique-se de que todas as dependências estão instaladas corretamente

### Como Reportar Problemas

1. Execute `python test_app.py` e inclua a saída
2. Descreva o comportamento esperado vs. observado
3. Inclua informações do sistema (OS, Python version, hardware)

