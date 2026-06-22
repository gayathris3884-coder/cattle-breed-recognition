import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model(
    "models/fine_tuned_model.keras"
)

class_names = [
    "Gir",
    "Holstein_Friesian",
    "Jaffrabadi",
    "Jersey",
    "Murrah",
    "Nili_Ravi",
    "Red_Sindhi",
    "Sahiwal",
    "Tharparkar"
]

img_path = input("Enter image path: ").strip().strip('"')

img = image.load_img(
    img_path,
    target_size=(224,224)
)

img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print(f"\nBreed: {predicted_class}")
print(f"Confidence: {confidence:.2f}%")