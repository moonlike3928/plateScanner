import cv2

def capture_frame():
    camera = cv2.VideoCapture(0)  # Pi Camera
    ret, frame = camera.read()
    camera.release()
    
    if not ret:
        print("[ERROR] Failed to capture frame")
        return None
    
    return frame
