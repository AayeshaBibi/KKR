# 🧠 MNIST Digit Classification using ANN (Artificial Neural Network)

This project demonstrates how to build and train an Artificial Neural Network (ANN) using TensorFlow and Keras to classify handwritten digits from the MNIST dataset. The trained model achieves over **98% accuracy** and can also predict digits from your own hand-drawn images.


## 📦 Requirements

Make sure you have Python 3.8 or higher installed on your system.

### Install Required Libraries

#### Using pip:

pip install tensorflow numpy pillow


#### Using Anaconda:

conda create -n mnist_env python=3.9
conda activate mnist_env
pip install tensorflow numpy pillow


## 🚀 How to Use This Project

### ✅ STEP 1: Train the ANN Model

1. Open a terminal or command prompt.
2. Navigate to the project directory where `mnist_ann.py` is located.
3. Run the training script:

python mnist_ann.py

This will:

* Load the MNIST dataset (built-in)
* Preprocess and normalize the data
* Train the ANN model
* Save the model as `mnist_ann_model.keras`


### 🖌️ STEP 2: Create Your Own Handwritten Digit Image

1. Open any drawing tool like **MS Paint**.
2. Draw a **black digit (0–9)** on a **white background**.
3. Save the image as `digit.png` in the same project folder.

**Tips for better results:**

* Use a **thick brush**
* Keep the digit centered
* Avoid any background noise
* Maintain a white background and black digit


### 🔍 STEP 3: Predict the Digit

1. Ensure the trained model (`mnist_ann_model.keras`) and `digit.png` image are present in the same folder.
2. Run the prediction script:

python predict_digit.py


The script will:

* Load and preprocess `digit.png`
* Resize and normalize the image
* Load the trained ANN model
* Output the predicted digit in the terminal

**Example Output:**

Predicted Digit: 7


## ⚠️ Troubleshooting and Tips

**Wrong predictions?**

* Ensure image is named `digit.png`
* Use **black on white background**
* Keep the digit bold, clean, and centered
* Do not crop the digit too closely

**Model not loading?**

* Make sure `mnist_ann_model.keras` was generated after training
* Ensure TensorFlow and required libraries are properly installed


## 📈 Improving Model Accuracy

To further improve the model performance:

* ✔️ Switch to a **CNN (Convolutional Neural Network)** — better suited for image data
* ✔️ Apply **image preprocessing techniques** like thresholding, centering, or smoothing (use OpenCV)
* ✔️ Use **data augmentation** (rotation, scaling, shift) during training for better generalization


## 📧 Contact

If you face any issues or have questions:

**Email:** [hashirkhan462002@gmail.com](mailto:hashirkhan462002@gmail.com)


## ⭐ Credits

* MNIST Dataset by [Yann LeCun](http://yann.lecun.com/exdb/mnist/)
* TensorFlow and Keras open-source libraries
