from django.urls import path
from .views import survey_view, thank_you_view, analysis_view

urlpatterns = [
    path('survey/', survey_view, name='survey'),
    path('thank_you/', thank_you_view, name='thank_you'),
    path('analysis/', analysis_view, name='analysis'),
]
