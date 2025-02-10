import cv2
import time
from camera import capture_frame
from plate_detector import detect_plate
from ocr import recognize_plate
from database import log_plate
from ui import update_display

def main():
    print("[INFO] Starting License Plate Scanner...")
    
    while True:
        frame = capture_frame()  # Capture image from Pi Camera
        plate_img = detect_plate(frame)  # Detect plate
        
        if plate_img is not None:
            plate_text = recognize_plate(plate_img)  # Extract text
            if plate_text:
                log_plate(plate_text)  # Save to database
                update_display(plate_text)  # Update UI
                print(f"[DETECTED] {plate_text}")

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
