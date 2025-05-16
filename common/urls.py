from django.urls import path
from common import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('abc/', views.Common.home,name="home"),
    path('about/', views.Common.about,name='about'),
    path('courses/', views.Common.courses,name='courses'),
    path('our-teams/', views.Common.ourteam,name='ourteams'),
    path('contact/', views.Common.contact,name='contactus'),
    # path('getdata/', views.Registration.as_view(),name='get-data'),
    path('registration_form/', views.Common.registration_form, name="registration_form"),
    path('registration/', views.Common.registration,name='registration'),
    path('login_from/', views.Common.login_form, name="login_from"),   
    path('login/', views.Common.login, name="login"),
    

]

# urlpatterns = [
    
#     # Your other URL patterns
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)