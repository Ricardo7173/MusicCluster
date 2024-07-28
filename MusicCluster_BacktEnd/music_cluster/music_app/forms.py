from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = [
            'instrument', 'rhythm', 'lyrics', 'language', 'listening_scenario', 
            'musical_personality', 'favorite_genre', 'favorite_artist', 
            'listening_platform', 'production_quality'
        ]
        
        widgets = {
            'instrument': forms.RadioSelect(choices=[
                ('Guitarra eléctrica', 'Guitarra eléctrica'),
                ('Piano', 'Piano'),
                ('Sintetizador', 'Sintetizador'),
                ('Violín', 'Violín'),
                ('Batería', 'Batería'),
                ('Percusión latina', 'Percusión latina'),
            ]),
            'rhythm': forms.RadioSelect(choices=[
                ('Rápido y enérgico', 'Rápido y enérgico'),
                ('Suave y relajante', 'Suave y relajante'),
                ('Ritmo bailable', 'Ritmo bailable'),
                ('Complejo y variado', 'Complejo y variado'),
                ('Constante y repetitivo', 'Constante y repetitivo'),
            ]),
            'lyrics': forms.RadioSelect(choices=[
                ('Letras de amor y relaciones', 'Letras de amor y relaciones'),
                ('Letras sobre la vida cotidiana', 'Letras sobre la vida cotidiana'),
                ('Letras sociales y políticas', 'Letras sociales y políticas'),
                ('Letras abstractas y poéticas', 'Letras abstractas y poéticas'),
                ('Letras festivas y alegres', 'Letras festivas y alegres'),
            ]),
            'language': forms.RadioSelect(choices=[
                ('Inglés', 'Inglés'),
                ('Español', 'Español'),
                ('Francés', 'Francés'),
                ('Alemán', 'Alemán'),
                ('Italiano', 'Italiano'),
                ('Otro', 'Otro'),
            ]),
            'listening_scenario': forms.RadioSelect(choices=[
                ('En un concierto en vivo', 'En un concierto en vivo'),
                ('En un club o discoteca', 'En un club o discoteca'),
                ('En casa, relajado/a', 'En casa, relajado/a'),
                ('Mientras trabajo o estudio', 'Mientras trabajo o estudio'),
                ('En el gimnasio o haciendo ejercicio', 'En el gimnasio o haciendo ejercicio'),
            ]),
            'musical_personality': forms.RadioSelect(choices=[
                ('Me encanta la energía y la adrenalina de la música', 'Me encanta la energía y la adrenalina de la música'),
                ('Prefiero melodías suaves y relajantes', 'Prefiero melodías suaves y relajantes'),
                ('Disfruto de la música que me hace pensar o reflexionar', 'Disfruto de la música que me hace pensar o reflexionar'),
                ('Me gustan las canciones que puedo bailar', 'Me gustan las canciones que puedo bailar'),
                ('Valoro la originalidad y la experimentación en la música', 'Valoro la originalidad y la experimentación en la música'),
            ]),
            'favorite_genre': forms.RadioSelect(choices=[
                ('Rock', 'Rock'),
                ('Pop', 'Pop'),
                ('Hip-Hop/Rap', 'Hip-Hop/Rap'),
                ('Electrónica/Dance', 'Electrónica/Dance'),
                ('Clásica', 'Clásica'),
                ('Jazz', 'Jazz'),
                ('Reggaetón', 'Reggaetón'),
                ('Salsa/Bachata', 'Salsa/Bachata'),
                ('Otro', 'Otro'),
            ]),
            'favorite_artist': forms.RadioSelect(choices=[
                ('The Beatles', 'The Beatles'),
                ('Taylor Swift', 'Taylor Swift'),
                ('Kendrick Lamar', 'Kendrick Lamar'),
                ('Daft Punk', 'Daft Punk'),
                ('Ludwig van Beethoven', 'Ludwig van Beethoven'),
                ('Miles Davis', 'Miles Davis'),
                ('Bad Bunny', 'Bad Bunny'),
                ('Marc Anthony', 'Marc Anthony'),
                ('Otro', 'Otro'),
            ]),
            'listening_platform': forms.RadioSelect(choices=[
                ('Spotify', 'Spotify'),
                ('Apple Music', 'Apple Music'),
                ('YouTube', 'YouTube'),
                ('Amazon Music', 'Amazon Music'),
                ('Radio', 'Radio'),
                ('Otra', 'Otra'),
            ]),
            'production_quality': forms.RadioSelect(choices=[
                ('Muy importante', 'Muy importante'),
                ('Moderadamente importante', 'Moderadamente importante'),
                ('Poco importante', 'Poco importante'),
                ('No es importante', 'No es importante'),
            ]),
        }
