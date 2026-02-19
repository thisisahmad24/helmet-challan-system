import cv2
import time
from ultralytics import YOLO


class HelmetDetector:
    def __init__(self):
        print("Loading YOLO model...")
        self.model = YOLO("yolov8n.pt")
        print("Model loaded successfully.")

        self.last_violation_time = 0
        self.COOLDOWN_SECONDS = 10

    def detect_violation(self, frame):
        results = self.model(frame)
        boxes = results[0].boxes
        names = results[0].names

        violation_detected = False

        for box in boxes:
            class_id = int(box.cls[0])
            class_name = names[class_id]

            if class_name == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                person_crop = frame[y1:y2, x1:x2]

                helmet_present = self.check_helmet(person_crop)

                if not helmet_present:
                    violation_detected = True

        return violation_detected, results[0].plot()

    def check_helmet(self, person_crop):
        """
        Placeholder helmet detection logic.
        Later we replace this with real helmet model.
        """

        # TEMPORARY SIMULATION
        import random
        return random.choice([True, False])

    def start_camera(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        print("Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            violation, annotated_frame = self.detect_violation(frame)

            current_time = time.time()

            if violation and (current_time - self.last_violation_time > self.COOLDOWN_SECONDS):
                print("❌ Helmet violation detected!")
                self.last_violation_time = current_time

            cv2.imshow("Helmet Detection System", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
