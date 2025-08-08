# image_procc.py
# This script uses a pre-trained YOLOv8 model to detect grocery items.

from ultralytics import YOLO

# Load a powerful, pre-trained model specialized in grocery detection.
# This model will be downloaded automatically the first time it's used.
# You can replace 'yolov8m-grocery-store.pt' with your own 'best.pt' if you train one.
model = YOLO('yolov8m.pt') 

def detect_objects(image_path: str) -> list[str]:
    """
    Detects objects in an image using a pre-trained YOLOv8 model.

    Args:
        image_path (str): The path to the uploaded image file.

    Returns:
        list[str]: A list of unique detected object names.
    """
    try:
        print(f"Processing image: {image_path}")
        # Run inference on the image
        results = model(image_path)

        detected_items = set()  # Use a set to automatically handle duplicates
        unwanted_items = {"bottle","person","can", "carton", "box", "refrigerator", "container", "package", "plastic", "bowl", "glass", "metal", "cardboard", "wood", "potted plant"}

        # Process results
        for r in results:
            for c in r.boxes.cls:
                item_name = model.names[int(c)]
                # Only add items that are not in unwanted_items
                if item_name.lower() not in unwanted_items:
                    detected_items.add(item_name)
        
        print(f"Detected items: {list(detected_items)}")
        return list(detected_items)

    except Exception as e:
        print(f"An error occurred during object detection: {e}")
        return []

