from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = load_model("models/best_model.keras")

test_gen = ImageDataGenerator(rescale=1./255)

test_data = test_gen.flow_from_directory(
    "dataset/test",
    target_size=(224,224),
    batch_size=32,
    shuffle=False
)

loss, acc = model.evaluate(test_data)

print(f"Test Accuracy: {acc*100:.2f}%")