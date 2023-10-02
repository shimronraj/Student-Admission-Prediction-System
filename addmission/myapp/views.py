from django.shortcuts import render
import pandas as pd
from xgboost import XGBRegressor
from .forms import CollegePredictionForm
import joblib

# Load the trained XGBoost model here
regressor = joblib.load('D:\\MARIAN\\NOTES\\SEM3 NOTES\\PROJECT\\addmission_prediction\\addmission\\savedModel\\admission.joblib')
df = pd.read_csv("D:\\MARIAN\\NOTES\\SEM3 NOTES\\PROJECT\\addmission_prediction\\addmission\\myapp\\NoteBook\\admission.csv")

def index(request):
    return render(request, 'index.html')

def predict_college(request):
    form = CollegePredictionForm()

    if request.method == 'POST':
        form = CollegePredictionForm(request.POST)

        if form.is_valid():
            user_input = form.cleaned_data  # Get cleaned data from the form
            user_input_df = pd.DataFrame([user_input])

            # Rename columns to match the expected feature names
            user_input_df = user_input_df.rename(columns={
                'tenth_marks': '10th Marks',
                'twelfth_marks': '12th Marks',
                'lbs_rank': 'LBS Rank',
                'cgpa': 'CGPA',
            })

            user_pred = regressor.predict(user_input_df)
            user_pred_rounded = round(user_pred[0])

            # Convert the predicted index back to college name
            colog = df['College'].unique()
            predicted_college = colog[user_pred_rounded - 1]

            context = {
                'form': form,
                'predicted_college': predicted_college,
            }
            return render(request, 'predict_college.html', context)

    # Handle GET requests or other cases
    context = {'form': form}
    return render(request, 'predict_college.html', context)
