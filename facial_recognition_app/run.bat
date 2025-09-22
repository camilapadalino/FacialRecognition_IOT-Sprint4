@echo off
echo Iniciando Aplicacao de Reconhecimento Facial...
echo.

REM Ativa o ambiente virtual
call venv\Scripts\activate.bat

REM Executa a aplicacao
python main.py

REM Pausa para ver mensagens de erro se houver
pause

