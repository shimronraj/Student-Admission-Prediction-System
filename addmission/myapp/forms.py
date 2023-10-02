# myapp/forms.py
from django import forms

class CollegePredictionForm(forms.Form):
    tenth_marks = forms.FloatField(label='10th Marks')
    twelfth_marks = forms.FloatField(label='12th Marks')
    lbs_rank = forms.IntegerField(label='LBS Rank')
    cgpa = forms.FloatField(label='CGPA')
