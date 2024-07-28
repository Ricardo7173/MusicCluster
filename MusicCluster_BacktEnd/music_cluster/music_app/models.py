from django.db import models

class SurveyResponse(models.Model):
    instrument = models.CharField(max_length=50, default='Guitarra eléctrica')
    rhythm = models.CharField(max_length=50, default='Rápido y enérgico')
    lyrics = models.CharField(max_length=50, default='Letras de amor y relaciones')
    language = models.CharField(max_length=50, default='Inglés')  # Valor por defecto
    listening_scenario = models.CharField(max_length=50, default='En casa, relajado/a')
    musical_personality = models.CharField(max_length=50, default='Me encanta la energía y la adrenalina de la música')
    favorite_genre = models.CharField(max_length=50, default='Rock')
    favorite_artist = models.CharField(max_length=50, default='The Beatles')
    listening_platform = models.CharField(max_length=50, default='Spotify')
    production_quality = models.CharField(max_length=50, default='Muy importante')
