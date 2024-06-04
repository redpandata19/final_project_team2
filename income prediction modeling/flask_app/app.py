from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import pickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/census_income_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class IncomeData(db.Model):
    __tablename__ = 'census'
    age = db.Column(db.Integer)
    workclass = db.Column(db.String(50))
    fnlwgt = db.Column(db.Integer)
    education = db.Column(db.String(20))
    educational_grade = db.Column(db.Integer)
    marital_status = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    relationship = db.Column(db.String(50))
    race = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    capital_gain = db.Column(db.Integer)
    capital_loss = db.Column(db.Integer)
    hours_worked_per_week = db.Column(db.Integer)
    native_country = db.Column(db.String(100))
    annual_income = db.Column(db.String(20))
    censusid = db.Column(db.Integer, primary_key=True)

# Load the trained model, scaler, and label encoders
best_model = keras.models.load_model('model.h5')
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)
with open('label_encoders.pkl', 'rb') as le_file:
    label_encoders = pickle.load(le_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the form data
        form_data = request.form
        input_data = {
            'age': int(form_data['age']),
            'workclass': 'Private',  # Default value
            'education': form_data['education'],
            'educational_grade': 10,  # Default value (assuming 10th grade)
            'marital_status': form_data['marital_status'],
            'occupation': 'Prof-specialty',  # Default value
            'relationship': 'Not-in-family',  # Default value
            'race': form_data['race'],
            'gender': form_data['gender'],
            'capital_gain': 0,  # Default value
            'capital_loss': 0,  # Default value
            'hours_worked_per_week': 40,  # Default value
            'native_country': 'United-States'  # Default value
        }

        # Encode categorical variables
        categorical_cols = ['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'gender', 'native_country']
        for col in categorical_cols:
            if input_data[col] in label_encoders[col].classes_:
                input_data[col] = label_encoders[col].transform([input_data[col]])[0]
            else:
                input_data[col] = label_encoders[col].transform(['United-States'])[0]

        # Ensure the data is in the correct order
        feature_order = ['age', 'workclass', 'education', 'educational_grade', 'marital_status', 'occupation', 'relationship', 'race', 'gender', 'capital_gain', 'capital_loss', 'hours_worked_per_week', 'native_country']
        input_data_ordered = {feature: input_data[feature] for feature in feature_order}

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data_ordered])
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction_prob = best_model.predict(input_scaled)[0][0]
        prediction_label = 'More than 50K' if prediction_prob > 0.5 else 'Less than 50K'
        prediction_confidence = prediction_prob if prediction_prob > 0.5 else 1 - prediction_prob
        prediction_confidence_percentage = round(prediction_confidence * 100, 2)

        return render_template('index.html', prediction_text=f'Predicted Annual Income: {prediction_label} with {prediction_confidence_percentage}% confidence')
    except KeyError as e:
        return render_template('index.html', prediction_text=f'Missing form field: {str(e)}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'An error occurred: {str(e)}')

@app.route('/chart-data', methods=['GET'])
def chart_data():
    query = db.session.query(IncomeData)
    data = query.all()

    education_data = {}
    hours_worked_data = []
    occupation_data = {}

    for record in data:
        # Education data
        if record.education not in education_data:
            education_data[record.education] = 0
        education_data[record.education] += 1

        # Hours worked and age data
        hours_worked_data.append({'x': record.hours_worked_per_week, 'y': record.age, 'v': record.hours_worked_per_week})

        # Occupation data
        if record.occupation not in occupation_data:
            occupation_data[record.occupation] = 0
        occupation_data[record.occupation] += 1

    chart_data = {
        'education': {
            'labels': list(education_data.keys()),
            'count': list(education_data.values())
        },
        'hours_worked': {
            'data': hours_worked_data
        },
        'occupation': {
            'labels': list(occupation_data.keys()),
            'count': list(occupation_data.values())
        }
    }

    return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)
