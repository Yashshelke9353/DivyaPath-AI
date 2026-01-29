from pathlib import Path
from app.module4.emotion_detector import detect_emotion

# Test image path (apni koi face image use karo)
IMAGE_PATH = Path(__file__).resolve().parents[2] / "data" / "test_face.jpg"

with open(IMAGE_PATH, "rb") as f:
    img_bytes = f.read()

emotion, confidence = detect_emotion(img_bytes)

print("Detected Emotion:", emotion)
print("Confidence:", round(confidence * 100, 2), "%")