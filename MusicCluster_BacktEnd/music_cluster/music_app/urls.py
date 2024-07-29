from django.urls import path
from .views import survey_view, thank_you_view, analysis_view, get_survey_results, export_survey_results

urlpatterns = [
    path('survey/', survey_view, name='survey'),
    path('thank_you/', thank_you_view, name='thank_you'),
    path('analysis/', analysis_view, name='analysis'),
    path('survey/results/', get_survey_results, name='get_survey_results'),
    path('survey/export/', export_survey_results, name='export_survey_results'),
]
