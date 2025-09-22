#!/usr/bin/env python3
"""
Script de teste para a aplicação de reconhecimento facial.
Testa os componentes principais sem interface gráfica.
"""

import sys
import os
import cv2
import numpy as np

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from face_detector import FaceDetector
from camera_manager import CameraManager


def test_face_detector():
    """
    Testa o detector facial com uma imagem de exemplo.
    """
    print("=== Testando Detector Facial ===")
    
    try:
        # Cria detector
        detector = FaceDetector()
        print("✓ Detector facial criado com sucesso")
        
        # Cria uma imagem de teste (simulada)
        test_image = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(test_image, (200, 150), (440, 330), (100, 100, 100), -1)
        cv2.circle(test_image, (280, 200), 20, (255, 255, 255), -1)  # Olho esquerdo
        cv2.circle(test_image, (360, 200), 20, (255, 255, 255), -1)  # Olho direito
        cv2.ellipse(test_image, (320, 260), (30, 15), 0, 0, 180, (255, 255, 255), -1)  # Boca
        
        # Testa detecção
        annotated_image, faces_info = detector.detect_faces(test_image)
        print(f"✓ Detecção executada. Faces encontradas: {len(faces_info)}")
        
        # Testa atualização de parâmetros
        detector.update_parameters(min_detection_confidence=0.7, show_landmarks=False)
        print("✓ Parâmetros atualizados com sucesso")
        
        # Libera recursos
        detector.release()
        print("✓ Recursos liberados")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro no teste do detector facial: {e}")
        return False


def test_camera_manager():
    """
    Testa o gerenciador de câmera.
    """
    print("\n=== Testando Gerenciador de Câmera ===")
    
    try:
        # Cria gerenciador
        camera = CameraManager()
        print("✓ Gerenciador de câmera criado")
        
        # Tenta iniciar câmera (pode falhar se não houver câmera)
        if camera.start_camera():
            print("✓ Câmera iniciada com sucesso")
            
            # Testa captura de frame
            ret, frame = camera.read_frame()
            if ret:
                print(f"✓ Frame capturado: {frame.shape}")
            else:
                print("⚠ Não foi possível capturar frame")
            
            # Testa informações da câmera
            info = camera.get_camera_info()
            print(f"✓ Informações da câmera: {info}")
            
            # Para câmera
            camera.stop_camera()
            print("✓ Câmera parada")
            
        else:
            print("⚠ Não foi possível iniciar câmera (normal se não houver câmera conectada)")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro no teste do gerenciador de câmera: {e}")
        return False


def test_imports():
    """
    Testa se todas as dependências estão instaladas corretamente.
    """
    print("=== Testando Importações ===")
    
    try:
        import cv2
        print(f"✓ OpenCV {cv2.__version__}")
        
        import mediapipe as mp
        print(f"✓ MediaPipe {mp.__version__}")
        
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import QTimer
        from PyQt5.QtGui import QImage
        print("✓ PyQt5")
        
        import numpy as np
        print(f"✓ NumPy {np.__version__}")
        
        return True
        
    except ImportError as e:
        print(f"✗ Erro de importação: {e}")
        return False


def main():
    """
    Executa todos os testes.
    """
    print("Iniciando testes da aplicação de reconhecimento facial...\n")
    
    tests = [
        test_imports,
        test_face_detector,
        test_camera_manager
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n=== Resultado dos Testes ===")
    print(f"Testes aprovados: {passed}/{total}")
    
    if passed == total:
        print("✓ Todos os testes passaram! A aplicação está pronta para uso.")
        return 0
    else:
        print("⚠ Alguns testes falharam. Verifique as dependências e configurações.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

