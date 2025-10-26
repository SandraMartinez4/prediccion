from django.contrib import admin
from django.urls import path
from predictor import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form_view, name='form_view'),
]
