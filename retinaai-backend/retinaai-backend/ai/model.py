import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

# -----------------------------
# Load TFLite model (only once)
# -----------------------------

print("Loading RetinaAI TFLite model...")

interpreter = tf.lite.Interpreter(model_path="ai/retinaai_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Model loaded successfully")


# -----------------------------
# Class labels
# -----------------------------

labels = [
    "No_DR",
    "Mild",
    "Moderate",
    "Severe",
    "Proliferative_DR"
]

IMG_SIZE = 300


# -----------------------------
# Retina Cropping
# -----------------------------

def crop_retina(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        return cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    c = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(c)

    img = img[y:y+h, x:x+w]

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    return img


# -----------------------------
# CLAHE Enhancement
# -----------------------------

def clahe_enhancement(img):

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))

    img = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return img


# -----------------------------
# Image Preprocessing
# -----------------------------

def preprocess(image):

    image = image.convert("RGB")

    img = np.array(image)

    img = crop_retina(img)

    img = clahe_enhancement(img)

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    # same preprocessing used during EfficientNet training
    img = preprocess_input(img)

    img = np.expand_dims(img, axis=0).astype(np.float32)

    return img


# -----------------------------
# Prediction
# -----------------------------

def predict(image):

    img = preprocess(image)

    interpreter.set_tensor(input_details[0]['index'], img)

    interpreter.invoke()

    preds = interpreter.get_tensor(output_details[0]['index'])[0]

    index = int(np.argmax(preds))

    return {
        "diagnosis": labels[index],
        "confidence": float(preds[index]),
        "probabilities": preds.tolist()
    }