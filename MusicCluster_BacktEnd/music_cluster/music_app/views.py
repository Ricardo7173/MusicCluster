from django.shortcuts import render, redirect
from .forms import SurveyForm
from .kmeans_analysis import run_kmeans
from .models import SurveyResponse
import pickle
import os
import pandas as pd
from django.http import JsonResponse
from django.http import HttpResponse
import openpyxl
from io import BytesIO

def export_survey_results(request):
    # Obtener los datos de la base de datos
    results = list(SurveyResponse.objects.all().values())

    # Crear un libro de trabajo de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Survey Results'

    # Encabezados
    headers = ['ID', 'Instrument', 'Rhythm', 'Lyrics', 'Language', 'Listening Scenario', 
               'Musical Personality', 'Favorite Genre', 'Favorite Artist', 'Listening Platform', 
               'Production Quality']
    ws.append(headers)

    # Agregar los datos a la hoja
    for result in results:
        ws.append([
            result['id'],
            result['instrument'],
            result['rhythm'],
            result['lyrics'],
            result['language'],
            result['listening_scenario'],
            result['musical_personality'],
            result['favorite_genre'],
            result['favorite_artist'],
            result['listening_platform'],
            result['production_quality']
        ])

    # Guardar el libro en un buffer de memoria
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # Crear una respuesta HTTP
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=survey_results.xlsx'

    return response

def get_survey_results(request):
    if request.method == 'GET':
        results = list(SurveyResponse.objects.all().values())
        return JsonResponse(results, safe=False)

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            new_response = form.save()

            # Cargar el modelo K-Means
            model_path = os.path.join(os.path.dirname(__file__), 'kmeans_model.pkl')
            with open(model_path, 'rb') as f:
                kmeans = pickle.load(f)

            # Preparar los datos de la nueva respuesta
            new_data = pd.DataFrame([{
                'instrument': new_response.instrument,
                'rhythm': new_response.rhythm,
                'lyrics': new_response.lyrics,
                'language': new_response.language,
                'listening_scenario': new_response.listening_scenario,
                'musical_personality': new_response.musical_personality,
                'favorite_genre': new_response.favorite_genre,
                'favorite_artist': new_response.favorite_artist,
                'listening_platform': new_response.listening_platform,
                'production_quality': new_response.production_quality
            }])
            new_data_encoded = pd.get_dummies(new_data)

            # Asegurarse de que las columnas coinciden con el modelo entrenado
            model_columns = kmeans.feature_names_in_
            missing_cols = set(model_columns) - set(new_data_encoded.columns)
            for col in missing_cols:
                new_data_encoded[col] = 0

            new_data_encoded = new_data_encoded[model_columns]

            # Hacer la predicción del clúster
            cluster = kmeans.predict(new_data_encoded)

            # Determinar el género predominante en ese clúster
            all_responses = pd.DataFrame(list(SurveyResponse.objects.all().values()))
            all_responses['cluster'] = kmeans.predict(pd.get_dummies(all_responses[[
                'instrument', 'rhythm', 'lyrics', 'language', 'listening_scenario',
                'musical_personality', 'favorite_genre', 'favorite_artist', 
                'listening_platform', 'production_quality'
            ]]))

            cluster_data = all_responses[all_responses['cluster'] == cluster[0]]
            predominant_genre = cluster_data['favorite_genre'].mode()[0]

            return render(request, 'music_app/thank_you.html', {'predicted_genre': predominant_genre})
    else:
        form = SurveyForm()
    return render(request, 'music_app/survey.html', {'form': form})

def thank_you_view(request):
    predicted_genre = request.GET.get('predicted_genre')
    return render(request, 'music_app/thank_you.html', {'predicted_genre': predicted_genre})

def analysis_view(request):
    run_kmeans()
    return render(request, 'music_app/analysis.html')
