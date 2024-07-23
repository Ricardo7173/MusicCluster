from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = [
            'age', 'gender', 'favorite_genre', 'listening_hours_per_week',
            'favorite_artist', 'concert_attendance', 'device_preference'
        ]
