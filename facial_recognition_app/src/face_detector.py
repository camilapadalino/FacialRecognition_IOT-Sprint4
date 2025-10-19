import cv2
import mediapipe as mp
import numpy as np
from typing import List, Tuple, Optional


class FaceDetector:
    """
    Classe para detecção e identificação facial usando MediaPipe e OpenCV.
    """
    
    def __init__(self, 
                 min_detection_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5):
        """
        Inicializa o detector facial.
        
        Args:
            min_detection_confidence: Confiança mínima para detecção (0.0 - 1.0)
            min_tracking_confidence: Confiança mínima para rastreamento (0.0 - 1.0)
        """
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Configuração do detector de faces
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=0,  # 0 para faces próximas (< 2m), 1 para faces distantes
            min_detection_confidence=min_detection_confidence
        )
        
        # Configuração do detector de landmarks faciais
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=5,
            refine_landmarks=True,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        
        # Parâmetros ajustáveis
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.show_landmarks = True
        self.show_bounding_box = True
        self.show_face_id = True
        
        # Contador de faces detectadas
        self.face_counter = 0
        
    def update_parameters(self, 
                         min_detection_confidence: Optional[float] = None,
                         min_tracking_confidence: Optional[float] = None,
                         show_landmarks: Optional[bool] = None,
                         show_bounding_box: Optional[bool] = None,
                         show_face_id: Optional[bool] = None):
        """
        Atualiza os parâmetros do detector.
        """
        if min_detection_confidence is not None:
            self.min_detection_confidence = min_detection_confidence
            # Recria o detector com novos parâmetros
            self.face_detection = self.mp_face_detection.FaceDetection(
                model_selection=0,
                min_detection_confidence=min_detection_confidence
            )
            self.face_mesh = self.mp_face_mesh.FaceMesh(
                static_image_mode=False,
                max_num_faces=5,
                refine_landmarks=True,
                min_detection_confidence=min_detection_confidence,
                min_tracking_confidence=self.min_tracking_confidence
            )
            
        if min_tracking_confidence is not None:
            self.min_tracking_confidence = min_tracking_confidence
            self.face_mesh = self.mp_face_mesh.FaceMesh(
                static_image_mode=False,
                max_num_faces=5,
                refine_landmarks=True,
                min_detection_confidence=self.min_detection_confidence,
                min_tracking_confidence=min_tracking_confidence
            )
            
        if show_landmarks is not None:
            self.show_landmarks = show_landmarks
            
        if show_bounding_box is not None:
            self.show_bounding_box = show_bounding_box
            
        if show_face_id is not None:
            self.show_face_id = show_face_id
    
    def detect_faces(self, image: np.ndarray) -> Tuple[np.ndarray, List[dict]]:
        """
        Detecta faces na imagem e retorna a imagem anotada e informações das faces.
        
        Args:
            image: Imagem de entrada (BGR)
            
        Returns:
            Tuple contendo:
            - Imagem anotada com detecções
            - Lista de dicionários com informações das faces detectadas
        """
        # Converte BGR para RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Processa a imagem
        detection_results = self.face_detection.process(rgb_image)
        mesh_results = self.face_mesh.process(rgb_image)
        
        # Copia a imagem para anotação
        annotated_image = image.copy()
        faces_info = []
        
        # Processa detecções de faces
        if detection_results.detections:
            for idx, detection in enumerate(detection_results.detections):
                # Extrai informações da detecção
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = image.shape
                
                # Converte coordenadas relativas para absolutas
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)
                
                # Informações da face
                face_info = {
                    'id': f'Face_{idx + 1}',
                    'confidence': detection.score[0],
                    'bbox': (x, y, width, height),
                    'center': (x + width // 2, y + height // 2)
                }
                faces_info.append(face_info)
                
                # Desenha bounding box se habilitado
                if self.show_bounding_box:
                    cv2.rectangle(annotated_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
                    
                    # Adiciona texto com confiança
                    confidence_text = f'{face_info["confidence"]:.2f}'
                    cv2.putText(annotated_image, confidence_text, (x, y - 10), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                # Adiciona ID da face se habilitado
                if self.show_face_id:
                    cv2.putText(annotated_image, face_info['id'], (x, y + height + 20), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        # Processa landmarks faciais
        if mesh_results.multi_face_landmarks and self.show_landmarks:
            for face_landmarks in mesh_results.multi_face_landmarks:
                # Desenha landmarks faciais
                self.mp_drawing.draw_landmarks(
                    annotated_image,
                    face_landmarks,
                    self.mp_face_mesh.FACEMESH_CONTOURS,
                    None,
                    self.mp_drawing_styles.get_default_face_mesh_contours_style()
                )
                

        
        return annotated_image, faces_info
    
    def get_face_encoding(self, image: np.ndarray, face_bbox: Tuple[int, int, int, int]) -> Optional[np.ndarray]:
        """
        Extrai características da face para identificação (versão simplificada).
        
        Args:
            image: Imagem original
            face_bbox: Bounding box da face (x, y, width, height)
            
        Returns:
            Vetor de características da face ou None se não conseguir extrair
        """
        try:
            x, y, w, h = face_bbox
            
            # Extrai a região da face
            face_roi = image[y:y+h, x:x+w]
            
            # Redimensiona para tamanho padrão
            face_resized = cv2.resize(face_roi, (128, 128))
            
            # Converte para escala de cinza
            face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
            
            # Calcula histograma como característica simples
            hist = cv2.calcHist([face_gray], [0], None, [256], [0, 256])
            
            # Normaliza o histograma
            hist = hist.flatten()
            hist = hist / (np.sum(hist) + 1e-7)
            
            return hist
            
        except Exception as e:
            print(f"Erro ao extrair características da face: {e}")
            return None
    
    def compare_faces(self, encoding1: np.ndarray, encoding2: np.ndarray, threshold: float = 0.6) -> bool:
        """
        Compara duas codificações de face para verificar se são da mesma pessoa.
        
        Args:
            encoding1: Primeira codificação
            encoding2: Segunda codificação
            threshold: Limiar de similaridade
            
        Returns:
            True se as faces são similares, False caso contrário
        """
        try:
            # Calcula correlação entre histogramas
            correlation = cv2.compareHist(encoding1, encoding2, cv2.HISTCMP_CORREL)
            return correlation > threshold
        except Exception as e:
            print(f"Erro ao comparar faces: {e}")
            return False
    
    def release(self):
        """
        Libera recursos do detector.
        """
        if hasattr(self, 'face_detection'):
            self.face_detection.close()
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()