#!/usr/bin/env python3
"""
Aplicação de Reconhecimento Facial - IOT & JOB
Desenvolvida usando OpenCV, MediaPipe e PyQt5

Este é o arquivo principal para executar a aplicação.
"""

import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importa e executa a aplicação principal
from gui_application import main

if __name__ == "__main__":
    main()

