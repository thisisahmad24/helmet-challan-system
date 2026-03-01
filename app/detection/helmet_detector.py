import cv2
import time
import os
from datetime import datetime
from ultralytics import YOLO


class HelmetDetector:
    def __init__(self, person_model_path="yolov8n.pt", helmet_model_path=None):
        """
        Initialize Helmet Detection System
        """
        print("🚀 Loading YOLO models...")

        # Person detection model
        self.person_model = YOLO(person_model_path)

        # Helmet detection model (custom)
        self.helmet_model = YOLO(helmet_model_path) if helmet_model_path else None

        print("✅ Models loaded successfully.")

        self.last_violation_time = 0
        self.COOLDOWN_SECONDS = 10

        # Create violations folder
        if not os.path.exists("violations"):
            os.makedirs("violations")

    def detect_violation(self, frame):
        """
        Detect persons and check helmet presence
        """
        frame = cv2.resize(frame, (640, 480))
        results = self.person_model(frame, conf=0.25)

        boxes = results[0].boxes
        names = results[0].names
        print("Detected objects:", len(boxes))

        violation_detected = False

        for box in boxes:
            class_id = int(box.cls[0])
            class_name = names[class_id]

            if class_name.lower() == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                person_crop = frame[y1:y2, x1:x2]

                if not self.check_helmet(person_crop):
                    violation_detected = True
                    cv2.putText(frame, "NO HELMET", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        annotated_frame = results[0].plot()
        return violation_detected, annotated_frame

    def check_helmet(self, person_crop):
        """
        Detect helmet in cropped person frame.
        If helmet_model not set, fallback to random detection for testing.
        """
        if person_crop.size == 0:
            return True

        if self.helmet_model:
            results = self.helmet_model(person_crop, conf=0.4)
            helmet_boxes = results[0].boxes
            helmet_names = results[0].names
            for box in helmet_boxes:
                class_id = int(box.cls[0])
                class_name = helmet_names[class_id]
                if class_name.lower() == "helmet":
                    return True
            return False
        else:
            # Temporary random detection placeholder
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

            cv2.imshow("Helmet Detection System", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()