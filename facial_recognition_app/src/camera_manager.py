import cv2
import numpy as np
from typing import Optional, Tuple


class CameraManager:
    """
    Classe para gerenciar a captura de vídeo da câmera.
    """
    
    def __init__(self, camera_index: int = 0, width: int = 640, height: int = 480):
        """
        Inicializa o gerenciador da câmera.
        
        Args:
            camera_index: Índice da câmera (0 para câmera padrão)
            width: Largura do frame
            height: Altura do frame
        """
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.cap = None
        self.is_opened = False
        
    def start_camera(self) -> bool:
        """
        Inicia a captura da câmera.
        
        Returns:
            True se a câmera foi iniciada com sucesso, False caso contrário
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            
            if not self.cap.isOpened():
                print(f"Erro: Não foi possível abrir a câmera {self.camera_index}")
                return False
            
            # Configura resolução
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
            
            # Configura FPS
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            self.is_opened = True
            print(f"Câmera {self.camera_index} iniciada com sucesso")
            return True
            
        except Exception as e:
            print(f"Erro ao iniciar câmera: {e}")
            return False
    
    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """
        Lê um frame da câmera.
        
        Returns:
            Tuple contendo:
            - bool: True se o frame foi lido com sucesso
            - np.ndarray: Frame capturado ou None se houve erro
        """
        if not self.is_opened or self.cap is None:
            return False, None
        
        try:
            ret, frame = self.cap.read()
            
            if ret:
                # Espelha a imagem horizontalmente para efeito de espelho
                frame = cv2.flip(frame, 1)
                return True, frame
            else:
                return False, None
                
        except Exception as e:
            print(f"Erro ao ler frame: {e}")
            return False, None
    
    def get_camera_info(self) -> dict:
        """
        Obtém informações da câmera.
        
        Returns:
            Dicionário com informações da câmera
        """
        if not self.is_opened or self.cap is None:
            return {}
        
        try:
            info = {
                'width': int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                'height': int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                'fps': self.cap.get(cv2.CAP_PROP_FPS),
                'brightness': self.cap.get(cv2.CAP_PROP_BRIGHTNESS),
                'contrast': self.cap.get(cv2.CAP_PROP_CONTRAST),
                'saturation': self.cap.get(cv2.CAP_PROP_SATURATION),
                'hue': self.cap.get(cv2.CAP_PROP_HUE)
            }
            return info
        except Exception as e:
            print(f"Erro ao obter informações da câmera: {e}")
            return {}
    
    def set_camera_property(self, property_id: int, value: float) -> bool:
        """
        Define uma propriedade da câmera.
        
        Args:
            property_id: ID da propriedade (cv2.CAP_PROP_*)
            value: Valor a ser definido
            
        Returns:
            True se a propriedade foi definida com sucesso
        """
        if not self.is_opened or self.cap is None:
            return False
        
        try:
            return self.cap.set(property_id, value)
        except Exception as e:
            print(f"Erro ao definir propriedade da câmera: {e}")
            return False
    
    def change_resolution(self, width: int, height: int) -> bool:
        """
        Altera a resolução da câmera.
        
        Args:
            width: Nova largura
            height: Nova altura
            
        Returns:
            True se a resolução foi alterada com sucesso
        """
        if not self.is_opened or self.cap is None:
            return False
        
        try:
            success_w = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            success_h = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            
            if success_w and success_h:
                self.width = width
                self.height = height
                return True
            return False
            
        except Exception as e:
            print(f"Erro ao alterar resolução: {e}")
            return False
    
    def stop_camera(self):
        """
        Para a captura da câmera e libera recursos.
        """
        if self.cap is not None:
            self.cap.release()
            self.is_opened = False
            print("Câmera parada")
    
    def __del__(self):
        """
        Destrutor para garantir que a câmera seja liberada.
        """
        self.stop_camera()

