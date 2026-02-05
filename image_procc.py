from ultralytics import YOLO
import cv2
import os
from classifier.predict import classify_image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

YOLO_MODEL = os.path.join(BASE_DIR, "yolov8m.pt")
CROP_DIR = os.path.join(BASE_DIR, "temp_uploads")
CONF_THRESHOLD = 0.6

UNWANTED_CLASSES = {
    "person", "refrigerator", "oven", "microwave",
    "sink", "table", "chair", "bowl", "cup", "glass",
    "box", "carton", "container", "package",
    "plastic", "metal", "wood", "cardboard", "potted plant"
}

# Classes that should be classified by the custom classifier (bottles and cans)
CLASSIFY_CLASSES = {"bottle", "can"}

os.makedirs(CROP_DIR, exist_ok=True)

yolo = YOLO(YOLO_MODEL)


def detect_objects(image_path: str) -> list[str]:
    image = cv2.imread(image_path)
    results = yolo(image_path)

    groceries = set()
    crop_id = 0

    for r in results:
        if r.boxes is None:
            continue

        for box, cls_id in zip(r.boxes.xyxy, r.boxes.cls):
            yolo_label = yolo.names[int(cls_id)].lower()

            if yolo_label in UNWANTED_CLASSES:
                continue

            # If it's a bottle or can, classify it with the custom classifier
            if yolo_label in CLASSIFY_CLASSES:
                x1, y1, x2, y2 = map(int, box)
                crop = image[y1:y2, x1:x2]

                if crop.size == 0:
                    continue

                crop_path = os.path.join(CROP_DIR, f"crop_{crop_id}.jpg")
                cv2.imwrite(crop_path, crop)
                crop_id += 1

                label, conf = classify_image(crop_path)
                print(f"YOLO: {yolo_label} → CLASSIFIER: {label} ({conf:.2f})")

                if conf >= CONF_THRESHOLD:
                    groceries.add(label)

                os.remove(crop_path)
            else:
                # For other items (like vegetables), use YOLO label directly
                print(f"YOLO: {yolo_label} → DIRECT: {yolo_label}")
                groceries.add(yolo_label)

    return list(groceries)
