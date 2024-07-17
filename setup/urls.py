from django.contrib import admin
from django.urls import path, include

# Todas as requests que são feitas para um determinado app, serão definidas dentro do urls.py do mesmo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]
