from django.shortcuts import render, redirect
from .forms import SurveyForm
from .kmeans_analysis import run_kmeans

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = SurveyForm()
    return render(request, 'music_app/survey.html', {'form': form})

def thank_you_view(request):
    return render(request, 'music_app/thank_you.html')

def analysis_view(request):
    run_kmeans()
    return render(request, 'music_app/analysis.html')
