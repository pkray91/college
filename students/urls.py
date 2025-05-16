from django.urls import path
from students import views


urlpatterns = [
    path('payment/',views.Students.add_pay,name="add-data"),
]