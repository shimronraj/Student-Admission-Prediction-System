from .import views
from django.urls import path

app_name = 'myapp' 

urlpatterns = [
    path('', views.index, name="index"),
    path('predict_college',views.predict_college,name='predict_college')


    ]