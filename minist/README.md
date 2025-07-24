🧠 MNIST Digit Classification using ANN (Artificial Neural Network)

This project demonstrates how to train an ANN using TensorFlow and Keras
to classify handwritten digits from the MNIST dataset with 98%+ accuracy.
You can also test the model by predicting digits from your own hand-drawn images.

📁 Project Structure:

mnist_digit_classifier/
│
├── mnist_ann.py            --> Training the ANN model on MNIST
├── predict_digit.py        --> Predicting digit from a custom image
├── mnist_ann_model.keras   --> Saved trained model
├── digit.png               --> Your own handwritten digit image
└── README.txt              --> Project documentation


📦 Requirements:

Python 3.8 or higher

Install the required libraries:

> Using pip:
    pip install tensorflow numpy pillow

> Or using Anaconda:
    conda create -n mnist_env python=3.9
    conda activate mnist_env
    pip install tensorflow numpy pillow


🚀 How to Use:

STEP 1: Train the ANN model

    python mnist_ann.py

This will:
- Load the MNIST dataset
- Train the neural network
- Save the model as 'mnist_ann_model.keras'

STEP 2: Create Your Own Digit Image
- Open MS Paint or any drawing tool
- Draw a black digit (0-9) on a white background
- Save the image as 'digit.png' in the same folder

STEP 3: Predict Your Digit
    python predict_digit.py

This will load your image, preprocess it, and print the predicted digit.

Example Output:
    Predicted Digit: 7


⚠️ Common Issues:

Wrong predictions?
- Make sure digit is centered and clear
- Use black on white background
- Let the code resize and invert the image
- Keep file name as 'digit.png'

📈 Improving Accuracy:

Even better results can be achieved by:

✔ Switching to a CNN model (Convolutional Neural Network)
✔ Using image preprocessing and centering (OpenCV)
✔ Applying data augmentation during training

📧 Contact:
Email: hashirkhan462002@gmail.com  

⭐ Credits:
- MNIST dataset provided by Yann LeCun
- TensorFlow / Keras open source frameworks
