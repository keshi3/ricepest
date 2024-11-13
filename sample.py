from flask import Flask, render_template, request, redirect, url_for
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np

import os
from sklearn.tree import DecisionTreeClassifier
from pest_data2py import feature_mapping, data, clf, eradication_descriptions

app = Flask(__name__)

# Load the trained ResNet model for image classification
model = load_model('my_trained_model.keras')

# Ensure the images directory exists
UPLOAD_FOLDER = '/Users/jonaldpamintuan/Documents/FINAL RICE PEST/UPLOADS'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to get pest density category
def get_pest_density(pest_count):
    if pest_count < 5:
        return "Maritak"
    elif 5 <= pest_count <= 60:
        return "Marakal"
    elif 60 < pest_count <= 150:
        return "Sobra Karakal"
    elif pest_count > 150:
        return "Ali na Abilang"

# Function to get the recommended eradication technique
def get_eradication_technique(pest_type, season, pest_density):
    input_data = np.array([ 
        feature_mapping['pest_type'][pest_type], 
        feature_mapping['season'][season], 
        feature_mapping['pest_density'][pest_density] 
    ]).reshape(1, -1)
    
    prediction = clf.predict(input_data)[0]
    for technique, code in feature_mapping['eradication_technique'].items():
        if code == prediction:
            return technique, eradication_descriptions[technique]

# Combine the prediction logic for pest eradication
def predict_recommendation(pest_type, season, pest_count):
    pest_density_category = get_pest_density(pest_count)
    technique_name, technique_description = get_eradication_technique(
        pest_type, season, pest_density_category
    )
    return technique_name, technique_description

# Route for the landing page (INDEX.html)
@app.route('/')
def index():
    return render_template('INDEX.html')

# Route for the intermediate page (PAGE1.html)
@app.route('/page1')
def page1():
    return render_template('PAGE1.html')

# Route for the image classification (main PAGE.html)
@app.route('/main', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        # Retrieve image from form
        imagefile = request.files['imagefile']
        image_path = "./UPLOADS/" + imagefile.filename
        imagefile.save(image_path)

        # Preprocess the image for the model
        image = load_img(image_path, target_size=(180, 180))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)

        # Make a prediction using the model
        yhat = model.predict(image)

        # Decode the prediction based on class labels
        class_labels = ['Green Leafhopper', 'Leaf Folder', 'Rice Bug', 'Stem Borer']  # Your class labels
        predicted_class = class_labels[yhat.argmax()]  # Get the class with the highest predicted probability

        # Classification result with confidence
        classification = f'{predicted_class} ({yhat.max()*100:.2f}%)'

        # Pass the prediction result to the template
        return render_template('PAGE.html', prediction=classification)

    return render_template('PAGE.html')

# Route for the recommendation system (PAGE2.html)
@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        # Retrieve form data for the recommendation system
        pest_type = request.form.get("pest_type")
        season = request.form.get("season")
        pest_count = float(request.form.get("pest_count"))

        # Generate recommendation based on input
        technique_name, technique_description = predict_recommendation(pest_type, season, pest_count)

        # Pass the recommendation to the template
        return render_template('PAGE2.html', 
                               technique_name=technique_name,
                               technique_description=technique_description)
    return render_template('PAGE2.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
