from flask import Flask, render_template, request
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from pest_data import feature_mapping, data, clf, eradication_descriptions

app = Flask(__name__)

# Helper functions
def get_pest_density(pest_count):
    if pest_count < 5:
        return "Maritak"
    elif 5 <= pest_count <= 60:
        return "Marakal"
    elif 60 < pest_count <= 150:
        return "Sobra Karakal"
    elif pest_count > 150:
        return "Ali na Abilang"

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

def predict(pest_type, season, pest_count):
    pest_density_category = get_pest_density(pest_count)
    technique_name, technique_description = get_eradication_technique(
        pest_type, season, pest_density_category
    )
    return technique_name, technique_description

# Routes3
#@app.route("/", methods=["GET", "POST"])
#def home():
    #technique_name = ""
    #technique_description = ""
    
   #if request.method == "POST":
    #    pest_type = request.form["pest_type"]
     #   season = request.form["season"]
      #  pest_count = float(request.form["pest_count"])

        # Call the prediction function
       # technique_name, technique_description = predict(pest_type, season, pest_count)

  #  return render_template(
   #     "index.html", 
    #    technique_name=technique_name,
    #    technique_description=technique_description
    #)

#if __name__ == "__main__":
    #app.run(debug=True)

#