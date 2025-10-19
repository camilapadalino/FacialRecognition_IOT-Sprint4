import cv2
import threading
import time
from flask import Flask, jsonify
from flask_cors import CORS
from src.face_detector import FaceDetector
from src.camera_manager import CameraManager

app = Flask(__name__)
CORS(app)  # Habilita CORS para aceitar requisições de qualquer origem

# Variáveis globais para armazenar o estado da detecção
face_detection_data = {
    "faces_detected": False,
    "face_count": 0,
    "timestamp": None,
    "last_detection": None,
    "camera_active": False
}

# Instâncias globais
camera_manager = None
face_detector = None
detection_thread = None
stop_detection = False


def start_face_detection():
    """
    Inicia a detecção facial em uma thread separada.
    """
    global camera_manager, face_detector, detection_thread, stop_detection
    
    stop_detection = False
    
    # Inicializa os componentes
    camera_manager = CameraManager()
    face_detector = FaceDetector()
    
    if not camera_manager.start_camera():
        return False
    
    # Inicia a thread de detecção
    detection_thread = threading.Thread(target=detection_loop, daemon=True)
    detection_thread.start()
    
    face_detection_data["camera_active"] = True
    return True


def detection_loop():
    """
    Loop contínuo de detecção facial.
    """
    global camera_manager, face_detector, stop_detection, face_detection_data
    
    while not stop_detection and camera_manager:
        try:
            ret, frame = camera_manager.read_frame()
            
            if ret and frame is not None:
                # Processa detecção facial
                annotated_frame, faces_info = face_detector.detect_faces(frame)
                
                # Atualiza os dados globais
                face_detection_data["faces_detected"] = len(faces_info) > 0
                face_detection_data["face_count"] = len(faces_info)
                face_detection_data["timestamp"] = time.time()
                
                if faces_info:
                    face_detection_data["last_detection"] = {
                        "count": len(faces_info),
                        "timestamp": time.time()
                    }
                
        except Exception as e:
            print(f"Erro na detecção facial: {e}")
            break
    
    # Finaliza a câmera
    if camera_manager:
        camera_manager.stop_camera()
    
    face_detection_data["camera_active"] = False


def stop_face_detection():
    """
    Para a detecção facial.
    """
    global stop_detection, camera_manager, face_detector
    
    stop_detection = True
    
    if camera_manager:
        camera_manager.stop_camera()
        camera_manager = None
    
    if face_detector:
        face_detector.release()
        face_detector = None
    
    face_detection_data["camera_active"] = False


# ==================== ENDPOINTS DA API ====================

@app.route("/api/status", methods=["GET"])
def get_status():
    """
    Retorna o status geral do servidor.
    """
    return jsonify({
        "status": "online",
        "camera_active": face_detection_data["camera_active"],
        "message": "Servidor de Reconhecimento Facial ativo"
    }), 200


@app.route("/api/start", methods=["POST"])
def start_detection():
    """
    Inicia a detecção facial.
    """
    if face_detection_data["camera_active"]:
        return jsonify({
            "success": False,
            "message": "Detecção facial já está ativa"
        }), 400
    
    if start_face_detection():
        return jsonify({
            "success": True,
            "message": "Detecção facial iniciada com sucesso"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Erro ao iniciar a detecção facial"
        }), 500


@app.route("/api/stop", methods=["POST"])
def stop_detection():
    """
    Para a detecção facial.
    """
    stop_face_detection()
    return jsonify({
        "success": True,
        "message": "Detecção facial parada"
    }), 200


@app.route("/api/detection", methods=["GET"])
def get_detection():
    """
    Retorna o status atual da detecção facial.
    """
    return jsonify({
        "faces_detected": face_detection_data["faces_detected"],
        "face_count": face_detection_data["face_count"],
        "timestamp": face_detection_data["timestamp"],
        "last_detection": face_detection_data["last_detection"]
    }), 200


@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Verifica a saúde da API.
    """
    return jsonify({
        "status": "healthy",
        "camera_active": face_detection_data["camera_active"]
    }), 200


# ==================== INICIALIZAÇÃO ====================

if __name__ == "__main__":
    print("Iniciando Servidor de Reconhecimento Facial...")
    print("API disponível em: http://localhost:5000")
    print("\nEndpoints disponíveis:")
    print("  GET  /api/status       - Status do servidor")
    print("  POST /api/start        - Iniciar detecção facial")
    print("  POST /api/stop         - Parar detecção facial")
    print("  GET  /api/detection    - Obter status da detecção")
    print("  GET  /api/health       - Health check")
    
    # Inicia o servidor Flask
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)