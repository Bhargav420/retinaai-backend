import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input

# ---------------------------
# Model path
# ---------------------------

MODEL_PATH = "services/best_retina_model.keras"

classes = [
    "No_DR",
    "Mild",
    "Moderate",
    "Severe",
    "Proliferative_DR"
]

IMG_SIZE = 300

# ---------------------------
# Load model
# ---------------------------

print("Loading RetinaAI model...")

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False,
    safe_mode=False
)

print("Model loaded successfully")


# ---------------------------
# Retina cropping
# ---------------------------

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


# ---------------------------
# CLAHE enhancement
# ---------------------------

def clahe_enhancement(img):

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )

    cl = clahe.apply(l)

    merged = cv2.merge((cl,a,b))

    img = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return img


# ---------------------------
# Preprocess image
# ---------------------------

def preprocess_image(image_path):

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found")

    img = crop_retina(img)

    img = clahe_enhancement(img)

    img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))

    img = preprocess_input(img)

    img = np.expand_dims(img,axis=0)

    return img


# ---------------------------
# Prediction
# ---------------------------

def predict_retina(image_path):

    img = preprocess_image(image_path)

    pred = model.predict(img)

    pred_class = np.argmax(pred)

    confidence = float(np.max(pred))

    return {
        "diagnosis": classes[pred_class],
        "confidence": confidence,
        "probabilities": pred[0].tolist()
    }
