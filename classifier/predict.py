import os
import tensorflow as tf
import numpy as np
import cv2

# Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "grocery_classifier.h5")
CLASSES_PATH = os.path.join(BASE_DIR, "model", "classes.txt")

model = None
CLASS_NAMES = []


def load_model():
    global model, CLASS_NAMES

    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

        model = tf.keras.models.load_model(MODEL_PATH)

        with open(CLASSES_PATH, "r") as f:
            CLASS_NAMES = [line.strip() for line in f.readlines()]


def classify_image(image_path: str):
    load_model()

    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img, verbose=0)
    idx = int(np.argmax(preds))
    conf = float(preds[0][idx])

    return CLASS_NAMES[idx], conf
