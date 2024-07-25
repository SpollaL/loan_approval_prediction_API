from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import PredictionForm
import pickle
import pandas as pd

# Create your views here.
pipeline = pickle.load(open('../loan_model.pkl', 'rb'))

@api_view(['GET', 'POST'])
def predict_view(request):
    if request.POST:
        form = PredictionForm(request.POST)
        if form.is_valid():
            input_data = {}
            for key in form.cleaned_data.keys():
                input_data[key] = form.cleaned_data[key]

            df = pd.DataFrame(input_data, index=[0])
            prediction = pipeline.predict(df)
            form.save()
            # Render the results page
            return render(
                request,
                'prediction_results.html',
                {'prediction': prediction, 'form': form})
    else:
        form = PredictionForm()
    return render(request, 'prediction_form.html', {'form': form})
