import cv2
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ultralytics import YOLO

model = YOLO('C:\\Users\\angel\\PycharmProjects\\facial_recognition\\utes_model.pt')


def home(request):
    return render(request, 'users/home.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'Imagen no proporcionada'}, status=400)

        image_file = request.FILES['image']
        np_img = np.frombuffer(image_file.read(), np.uint8)
        frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        results = model.predict(source=frame)

        detected_person = None
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls.item())
                detected_person = model.names[class_id]
                break
        if detected_person:
            return JsonResponse({
                'mensaje': f'Hola, bienvenido {detected_person}!'
            })
        else:
            return JsonResponse({
                'mensaje': 'No se detectó a ninguna persona.'
            })

    elif request.method == 'GET':
        return render(request, 'users/login.html')

    return JsonResponse({'error': 'Método no permitido'}, status=405)
