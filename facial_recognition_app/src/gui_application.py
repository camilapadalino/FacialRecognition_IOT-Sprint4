import sys
import os
from datetime import datetime
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QSlider, QCheckBox, QPushButton,
                             QGroupBox, QGridLayout, QTextEdit, QSplitter, QFrame)
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QFont
from face_detector import FaceDetector
from camera_manager import CameraManagergit 


class VideoWidget(QLabel):
    """
    Widget personalizado para exibir o vídeo da câmera.
    """
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)
        self.setStyleSheet("border: 2px solid gray; background-color: black;")
        self.setAlignment(Qt.AlignCenter)
        self.setText("Câmera não iniciada")
        self.setScaledContents(True)
    
    def update_frame(self, cv_img):
        """
        Atualiza o frame exibido no widget.
        
        Args:
            cv_img: Imagem OpenCV (BGR)
        """
        try:
            # Converte BGR para RGB
            rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            
            # Cria QImage
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            # Converte para QPixmap e exibe
            pixmap = QPixmap.fromImage(qt_image)
            self.setPixmap(pixmap)
            
        except Exception as e:
            print(f"Erro ao atualizar frame: {e}")


class ParameterPanel(QWidget):
    """
    Painel de controle dos parâmetros do detector facial.
    """
    
    # Sinais para comunicar mudanças de parâmetros
    detection_confidence_changed = pyqtSignal(float)
    tracking_confidence_changed = pyqtSignal(float)
    show_landmarks_changed = pyqtSignal(bool)
    show_bounding_box_changed = pyqtSignal(bool)
    show_face_id_changed = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """
        Inicializa a interface do painel de parâmetros.
        """
        layout = QVBoxLayout()
        
        # Título
        title = QLabel("Parâmetros de Detecção")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Grupo de confiança
        confidence_group = QGroupBox("Confiança")
        confidence_layout = QGridLayout()
        
        # Confiança de detecção
        confidence_layout.addWidget(QLabel("Detecção:"), 0, 0)
        self.detection_slider = QSlider(Qt.Horizontal)
        self.detection_slider.setRange(10, 100)
        self.detection_slider.setValue(50)
        self.detection_slider.valueChanged.connect(self.on_detection_confidence_changed)
        confidence_layout.addWidget(self.detection_slider, 0, 1)
        
        self.detection_label = QLabel("0.50")
        confidence_layout.addWidget(self.detection_label, 0, 2)
        
        # Confiança de rastreamento
        confidence_layout.addWidget(QLabel("Rastreamento:"), 1, 0)
        self.tracking_slider = QSlider(Qt.Horizontal)
        self.tracking_slider.setRange(10, 100)
        self.tracking_slider.setValue(50)
        self.tracking_slider.valueChanged.connect(self.on_tracking_confidence_changed)
        confidence_layout.addWidget(self.tracking_slider, 1, 1)
        
        self.tracking_label = QLabel("0.50")
        confidence_layout.addWidget(self.tracking_label, 1, 2)
        
        confidence_group.setLayout(confidence_layout)
        layout.addWidget(confidence_group)
        
        # Grupo de visualização
        display_group = QGroupBox("Visualização")
        display_layout = QVBoxLayout()
        
        # Checkboxes para opções de visualização
        self.landmarks_checkbox = QCheckBox("Mostrar Landmarks Faciais")
        self.landmarks_checkbox.setChecked(True)
        self.landmarks_checkbox.stateChanged.connect(self.on_show_landmarks_changed)
        display_layout.addWidget(self.landmarks_checkbox)
        
        self.bbox_checkbox = QCheckBox("Mostrar Caixas Delimitadoras")
        self.bbox_checkbox.setChecked(True)
        self.bbox_checkbox.stateChanged.connect(self.on_show_bounding_box_changed)
        display_layout.addWidget(self.bbox_checkbox)
        
        self.face_id_checkbox = QCheckBox("Mostrar ID das Faces")
        self.face_id_checkbox.setChecked(True)
        self.face_id_checkbox.stateChanged.connect(self.on_show_face_id_changed)
        display_layout.addWidget(self.face_id_checkbox)
        
        display_group.setLayout(display_layout)
        layout.addWidget(display_group)
        
        # Espaçador
        layout.addStretch()
        
        self.setLayout(layout)
    
    def on_detection_confidence_changed(self, value):
        """
        Callback para mudança na confiança de detecção.
        """
        confidence = value / 100.0
        self.detection_label.setText(f"{confidence:.2f}")
        self.detection_confidence_changed.emit(confidence)
    
    def on_tracking_confidence_changed(self, value):
        """
        Callback para mudança na confiança de rastreamento.
        """
        confidence = value / 100.0
        self.tracking_label.setText(f"{confidence:.2f}")
        self.tracking_confidence_changed.emit(confidence)
    
    def on_show_landmarks_changed(self, state):
        """
        Callback para mudança na exibição de landmarks.
        """
        self.show_landmarks_changed.emit(state == Qt.Checked)
    
    def on_show_bounding_box_changed(self, state):
        """
        Callback para mudança na exibição de bounding boxes.
        """
        self.show_bounding_box_changed.emit(state == Qt.Checked)
    
    def on_show_face_id_changed(self, state):
        """
        Callback para mudança na exibição de IDs das faces.
        """
        self.show_face_id_changed.emit(state == Qt.Checked)


class InfoPanel(QWidget):
    """
    Painel de informações sobre as faces detectadas.
    """
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """
        Inicializa a interface do painel de informações.
        """
        layout = QVBoxLayout()
        
        # Título
        title = QLabel("Informações das Faces")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Área de texto para informações
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        self.info_text.setMaximumHeight(200)
        layout.addWidget(self.info_text)
        
        # Estatísticas
        stats_group = QGroupBox("Estatísticas")
        stats_layout = QGridLayout()
        
        stats_layout.addWidget(QLabel("Faces detectadas:"), 0, 0)
        self.faces_count_label = QLabel("0")
        stats_layout.addWidget(self.faces_count_label, 0, 1)
        
        stats_layout.addWidget(QLabel("FPS:"), 1, 0)
        self.fps_label = QLabel("0")
        stats_layout.addWidget(self.fps_label, 1, 1)
        
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        self.setLayout(layout)
    
    def update_info(self, faces_info, fps):
        """
        Atualiza as informações das faces detectadas.
        
        Args:
            faces_info: Lista de informações das faces
            fps: Taxa de quadros por segundo
        """
        # Atualiza contadores
        self.faces_count_label.setText(str(len(faces_info)))
        self.fps_label.setText(f"{fps:.1f}")
        
        # Atualiza texto de informações
        info_text = ""
        for i, face in enumerate(faces_info):
            info_text += f"Face {i+1}:\n"
            info_text += f"  ID: {face['id']}\n"
            info_text += f"  Confiança: {face['confidence']:.3f}\n"
            info_text += f"  Posição: {face['center']}\n"
            info_text += f"  Tamanho: {face['bbox'][2]}x{face['bbox'][3]}\n\n"
        
        if not faces_info:
            info_text = "Nenhuma face detectada"
        
        self.info_text.setText(info_text)


class FacialRecognitionApp(QMainWindow):
    """
    Aplicação principal de reconhecimento facial.
    """
    
    def __init__(self):
        super().__init__()
        self.camera_manager = None
        self.face_detector = None
        self.timer = None
        self.fps_counter = 0
        self.fps_timer = 0
        self.current_fps = 0
        
        self.init_ui()
        self.init_components()
    
    def init_ui(self):
        """
        Inicializa a interface principal.
        """
        self.setWindowTitle("Aplicação de Reconhecimento Facial - IOT & JOB")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout()
        
        # Splitter para dividir a tela
        splitter = QSplitter(Qt.Horizontal)
        
        # Painel esquerdo (vídeo)
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        # Widget de vídeo
        self.video_widget = VideoWidget()
        left_layout.addWidget(self.video_widget)
        
        # Botões de controle
        control_layout = QHBoxLayout()
        
        self.start_button = QPushButton("Iniciar Câmera")
        self.start_button.clicked.connect(self.start_camera)
        control_layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("Parar Câmera")
        self.stop_button.clicked.connect(self.stop_camera)
        self.stop_button.setEnabled(False)
        control_layout.addWidget(self.stop_button)
        
        left_layout.addLayout(control_layout)
        left_panel.setLayout(left_layout)
        
        # Painel direito (controles e informações)
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        
        # Painel de parâmetros
        self.parameter_panel = ParameterPanel()
        right_layout.addWidget(self.parameter_panel)
        
        # Separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        right_layout.addWidget(separator)
        
        # Painel de informações
        self.info_panel = InfoPanel()
        right_layout.addWidget(self.info_panel)
        
        right_panel.setLayout(right_layout)
        
        # Adiciona painéis ao splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([800, 400])
        
        main_layout.addWidget(splitter)
        central_widget.setLayout(main_layout)
    
    def init_components(self):
        """
        Inicializa os componentes da aplicação.
        """
        # Inicializa detector facial
        self.face_detector = FaceDetector()
        
        # Conecta sinais dos parâmetros
        self.parameter_panel.detection_confidence_changed.connect(
            lambda x: self.face_detector.update_parameters(min_detection_confidence=x)
        )
        self.parameter_panel.tracking_confidence_changed.connect(
            lambda x: self.face_detector.update_parameters(min_tracking_confidence=x)
        )
        self.parameter_panel.show_landmarks_changed.connect(
            lambda x: self.face_detector.update_parameters(show_landmarks=x)
        )
        self.parameter_panel.show_bounding_box_changed.connect(
            lambda x: self.face_detector.update_parameters(show_bounding_box=x)
        )
        self.parameter_panel.show_face_id_changed.connect(
            lambda x: self.face_detector.update_parameters(show_face_id=x)
        )
        
        # Timer para captura de vídeo
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        
        # Timer para FPS
        self.fps_timer = QTimer()
        self.fps_timer.timeout.connect(self.update_fps)
        self.fps_timer.start(1000)  # Atualiza FPS a cada segundo
    
    def start_camera(self):
        """
        Inicia a captura da câmera.
        """
        try:
            self.camera_manager = CameraManager()
            
            if self.camera_manager.start_camera():
                self.timer.start(30)  # ~33 FPS
                self.start_button.setEnabled(False)
                self.stop_button.setEnabled(True)
                self.video_widget.setText("")
                print("Câmera iniciada com sucesso")
            else:
                self.video_widget.setText("Erro ao iniciar câmera")
                print("Erro ao iniciar câmera")
                
        except Exception as e:
            self.video_widget.setText(f"Erro: {str(e)}")
            print(f"Erro ao iniciar câmera: {e}")
    
    def stop_camera(self):
        """
        Para a captura da câmera.
        """
        if self.timer:
            self.timer.stop()
        
        if self.camera_manager:
            self.camera_manager.stop_camera()
            self.camera_manager = None
        
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.video_widget.setText("Câmera parada")
        self.info_panel.update_info([], 0)
        print("Câmera parada")

    def update_frame(self):
        """
        Atualiza o frame do vídeo.
        """
        if not self.camera_manager:
            return
        
        try:
            ret, frame = self.camera_manager.read_frame()
            
            if ret and frame is not None:

                # Processa detecção facial
                annotated_frame, faces_info = self.face_detector.detect_faces(frame)
                
                # Atualiza widget de vídeo
                self.video_widget.update_frame(annotated_frame)
                
                # Atualiza informações
                self.info_panel.update_info(faces_info, self.current_fps)
                
                # Conta frames para FPS
                self.fps_counter += 1
                
                # Log de evento de detecção facial
                if faces_info:
                    self.log_face_detection_event(faces_info)
                
        except Exception as e:
            print(f"Erro ao atualizar frame: {e}")

    def log_face_detection_event(self, faces_info):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Face detectada: {len(faces_info)} faces.\n"
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'face_detection_log.txt')
        with open(log_file_path, "a") as f:
            f.write(log_entry)
        print(f"Log: {log_entry.strip()}")

    def update_fps(self):
        """
        Atualiza o contador de FPS.
        """
        self.current_fps = self.fps_counter
        self.fps_counter = 0
    
    def closeEvent(self, event):
        """
        Evento de fechamento da aplicação.
        """
        self.stop_camera()
        
        if self.face_detector:
            self.face_detector.release()
        
        event.accept()


def main():
    """
    Função principal da aplicação.
    """
    app = QApplication(sys.argv)
    
    # Configura estilo da aplicação
    app.setStyle('Fusion')
    
    # Cria e exibe a janela principal
    window = FacialRecognitionApp()
    window.show()
    
    # Inicia o loop da aplicação
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
