from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the saved model


def preprocess_image(image_path, target_size):
    # Load the image
    img = load_img(image_path, target_size=target_size)
    
    # Convert the image to a numpy array
    img_array = img_to_array(img)
    
    # Expand dimensions to match the input shape of the model (batch size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Normalize the image array (if your model was trained with normalized data)
    img_array = img_array / 255.0
    
    return img_array

def make_prediction( image_path, target_size=(224, 224)):
    # Preprocess the image
    model = load_model('malenoma.h5')
    preprocessed_image = preprocess_image(image_path, target_size)
    # Make prediction
    prediction = model.predict(preprocessed_image)
    if(prediction[0][0]>0.9):
        return 'Positive'
    return 'Negative'

# # Example usage
# image_path = 'path_to_your_image.jpg'
# prediction = make_prediction(model, image_path)

# print(f'Prediction: {prediction}')
