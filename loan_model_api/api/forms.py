from django import forms

class PredictionForm(forms.Form):
    # Define fields for the form
    Gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))
    Married = forms.ChoiceField(choices=(('No', 'No'), ('Yes', 'Yes')))
    Dependents = forms.IntegerField(max_value=10, min_value=0)
    Education = forms.ChoiceField(choices=(('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')))
    Self_Employed = forms.ChoiceField(choices=(('No', 'No'), ('Yes', 'Yes')))
    ApplicantIncome = forms.FloatField(min_value=0)
    CoapplicantIncome = forms.FloatField(min_value=0)
    LoanAmount = forms.IntegerField(min_value=0)
    Loan_Amount_Term = forms.IntegerField(min_value=0)
    Credit_History = forms.IntegerField(min_value=0, max_value=1)
    Property_Area = forms.ChoiceField(choices=(('Urban', 'Urban'), ('SemiUrban', 'SemiUrban'), ('Ruaral', 'Rural')))
