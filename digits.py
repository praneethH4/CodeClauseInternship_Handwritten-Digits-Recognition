# Function to predict a digit
def predict_digit(image):
    # Preprocess the image
    image = image.reshape(1, 28, 28).astype('float32') / 255.0
    # Predict the digit
    prediction = model.predict(image)
    return prediction.argmax()

# Test the function with a new image
index = 0  # Change the index to test different images
plt.imshow(x_test[index].reshape(28, 28), cmap='gray')
plt.title(f'Predicted: {predict_digit(x_test[index])}')
plt.show()
