from django.shortcuts import render

# Create your views here.


from django.views import View

class Students(View):
    
    def add_pay(request):
        return render(request, 'backend/name.html')