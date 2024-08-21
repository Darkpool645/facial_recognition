import os
#import glob
#import cv2
from django.conf import settings
from django.shortcuts import render, redirect

#from users.models import User
#from .forms import UserRegistrationForm
# from roboflow import Roboflow

#def register(request):
#    if request.method == 'POST':
#        form = UserRegistrationForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            user_folder = os.path.join(settings.MEDIA_ROOT, user.name)

            # Crear carpeta para almacenar las fotos si no existe
#            os.makedirs(user_folder, exist_ok=True)

            # Inicializar la cámara y capturar las fotos
#            cam = cv2.VideoCapture(0)
#            for i in range(500):
#                ret, frame = cam.read()
#                if not ret:
#                    break
#                img_name = os.path.join(user_folder, f'{user.name}_{i}.jpg')
#                cv2.imwrite(img_name, frame)
#            cam.release()

            # Subir las fotos a Roboflow sin especificar la versión
#            try:
#                rf = Roboflow(api_key=settings.ROBOFLOW_API_KEY)
#                project = rf.workspace(settings.ROBOFLOW_WORKSPACE).project(settings.ROBOFLOW_PROJECT)
#                for image_path in glob.glob(os.path.join(user_folder, '*.jpg')):
#                    project.upload(image_path, name=user.name)
#                print(f'Fotos del usuario {user.name} subidas a Roboflow con éxito.')
#            except Exception as e:
#                print(f'Error al subir las fotos a Roboflow: {e}')
#            finally:
                # Eliminar la carpeta del usuario y todas las fotos
#                if os.path.exists(user_folder):
#                    for file in glob.glob(os.path.join(user_folder, '*')):
#                        os.remove(file)
#                    os.rmdir(user_folder)
#                print(f'Carpeta del usuario {user.name} eliminada.')

#            return redirect('register_success')
#    else:
#        form = UserRegistrationForm()
#    return render(request, 'users/register.html', {'form': form})


#def register_success(request):
#    return render(request, 'users/register_success.html')


def home(request):
    return render(request, 'users/home.html')


def login(request):
    img_path = os.path.join(settings.MEDIA_ROOT, 'temp_login.jpg')
    try:
        print('hola mundo')
    except Exception as e:
        return render(request, 'users/login.html', {'error': e})
    return render(request, 'users/login.html')