import cv2
import time
import os
from datetime import datetime
from ultralytics import YOLO


class HelmetDetector:
    def __init__(self):
        print("🚀 Loading YOLO model...")
        self.model = YOLO("yolov8n.pt")  # Make sure file exists in project root
        print("✅ Model loaded successfully.")

        self.last_violation_time = 0
        self.COOLDOWN_SECONDS = 10

        # Create violations folder if not exists
        if not os.path.exists("violations"):
            os.makedirs("violations")

    def detect_violation(self, frame):
        # Resize frame for stable detection
        frame = cv2.resize(frame, (640, 480))

        # Run YOLO with confidence threshold
        results = self.model(frame, conf=0.25)

        boxes = results[0].boxes
        names = results[0].names

        print("Detected objects:", len(boxes))

        violation_detected = False

        for box in boxes:
            class_id = int(box.cls[0])
            class_name = names[class_id]

            if class_name == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Crop person region
                person_crop = frame[y1:y2, x1:x2]

                helmet_present = self.check_helmet(person_crop)

                if not helmet_present:
                    violation_detected = True

        # VERY IMPORTANT: return annotated frame
        annotated_frame = results[0].plot()

        return violation_detected, annotated_frame

    def check_helmet(self, person_crop):
        """
        Placeholder helmet detection logic.
        Replace later with real helmet model.
        """
        import random
        return random.choice([True, False])

    def save_violation_image(self, frame):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"violations/violation_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Evidence saved: {filename}")

    def start_camera(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("❌ Error: Could not open camera.")
            return

        print("🎥 Camera started. Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠ Failed to read frame.")
                break

            violation, annotated_frame = self.detect_violation(frame)

            current_time = time.time()

            if violation and (current_time - self.last_violation_time > self.COOLDOWN_SECONDS):
                print("🚨 Helmet violation detected!")
                self.save_violation_image(annotated_frame)
                self.last_violation_time = current_time

            # SHOW DETECTION FRAME (FIXED)
            cv2.imshow("Helmet Detection System", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
