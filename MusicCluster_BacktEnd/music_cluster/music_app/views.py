from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    return JsonResponse({"message": "Music Cluster API is running"})

@csrf_exempt
def process_data(request):
    if request.method == 'POST':
        # Por ahora, solo devolveremos un mensaje de éxito
        return JsonResponse({"message": "Endpoint en construcción"}, status=200)
    return JsonResponse({"error": "Método no permitido"}, status=405)
