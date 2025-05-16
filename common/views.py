from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout, authenticate, login
from django.views import View

class Common(View):
    """
    List all snippets, or create a new snippet.
    """
    
    # def get(self, request, format=None):
    #     data = User.objects.all()
    #     serilized_data = CouresesSerializer(data, many=True)
    #     return Response(serilized_data.data)
    
    def home(request):
        return render(request, 'frontend/p1.html')

    def about(request):
        return render(request, 'frontend/about.html')

    def courses(request):
        # data = Coureses.objects.all()
        # data = Coureses.objects.order_by('semester').all()
        data = Coureses.objects.all().order_by('-semester')
        # data = Coureses.objects.all().order_by('semester')
        # data = Coureses.objects.filter(title="math")
        # data = Coureses.objects.exclude(title="math")
        # data = Coureses.objects.get(title="math")
        # data = Coureses.objects.all().values()# return queryset and each record will be dict.
        # data = Coureses.objects.all().values_list('title','description')# return queryset and each record will be tuple.
        
        print(data,9999999999)
        for i in data:
            pass
            # print(type(i))
            # print(i.description)
        return render(request, 'frontend/courses.html',{"course":data})

    def ourteam(request):
        return render(request, 'frontend/ourteam.html')

    def contact(request):
        return render(request, 'frontend/contact.html')

    def registration_form(request):
        return render(request, 'backend/registration.html')
    
    def registration(request):
        
        user = User()
        email_id = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        confirm_password = request.POST.get('confirm_password')
        user.username = email_id.split('@')[0].split('.')[0]
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = email_id
        user.phone_number = request.POST.get('phone_number')
        user.user_type = user_type
        user.set_password(password)
        
        if not (email_id and password and confirm_password):
            messages.error(request, 'Please provide all the details!!')
            return render(request, 'backend/registration.html')
     
        if password != confirm_password:
            messages.error(request, 'Both passwords should match!!')
            return render(request, 'backend/registration.html')
    
        is_user_exists = User.objects.filter(email=email_id).exists()
    
        if is_user_exists:
            messages.error(request, 'User with this email id already exists. Please proceed to login!!')
            return render(request, 'backend/registration.html')
        
        if user_type is None:
            messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
            return render(request, 'backend/registration.html')
    
        username = email_id.split('@')[0].split('.')[0]
    
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists. Please use different username')
            return render(request, 'backend/registration.html')
        user.save()

        # if user_type == User.STAFF:
        #     Staffs.objects.create(admin=user)
        # elif user_type == User.STUDENT:
        #     Students.objects.create(admin=user)
        # elif user_type == User.HOD:
        #     AdminHOD.objects.create(admin=user)
        return redirect('login_from')
    
    def login_form(request):
        return render(request, 'backend/login_page.html')
    
    def login(request):
        user = User()
        email_id = request.GET.get('email')
        password = request.GET.get('password')
        if not (email_id and password):
            messages.error(request, "Please provide all the details!!")
            return render(request, 'backend/login_page.html')
    
        user = authenticate(request, email=email_id, password=password)
    
        if user is not None:
            login(request, user)
            data = User.objects.get(id=user.id)
            print(data,33333)
            return render(request, 'backend/students.html',{'user':data})
        else:
            messages.error(request, 'Invalid Login Credentials!!')
            return render(request, 'backend/login_page.html')
 
        
    
