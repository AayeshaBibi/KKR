import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps

# Load the model
model = load_model("mnist_ann_model.keras")

# Load the image
img = Image.open("digit.png").convert("L")  # Convert to grayscale

# Invert image (MNIST is white digit on black)
img = ImageOps.invert(img)

# Resize to 28x28
img = img.resize((28, 28))

# Convert to array
img_array = np.array(img)

# Normalize
img_array = img_array.astype("float32") / 255.0

# Flatten and reshape
img_array = img_array.reshape(1, 784)

# Predict
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

print("Predicted Digit:", predicted_class)