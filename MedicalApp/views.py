from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from MedicalApp.models import Signup,UserType,Medicine


# Create your views here.

class index(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context
class about(TemplateView):
    template_name='about.html'
class contact(TemplateView):
    template_name='contact.html'

class loginview(TemplateView):
    template_name='login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['Email']
        password = request.POST['Password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "pharmacy":
                    return redirect('/pharmacy')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})

class signup(TemplateView):
    template_name="signup.html"
    def post(self, request, *args, **kwargs):
        name = request.POST['Username']
        email = request.POST['Email']
        phone = request.POST['Phone']
        address = request.POST['Address']
        district = request.POST['District']
        password = request.POST['Password']

      
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'signup.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Signup()# call the model
            reg.public_user = user

            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.address=address
            reg.district=district
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            # messages="Registered Successfully"

            return render(request, 'index.html', {'message': "successfully added"})

class View_Medicines_User(TemplateView):
    template_name='shop.html'
    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context
    
# class single_medicine(TemplateView):
#     template_name='shop-single.html'
#     def get_context_data(self, **kwargs):
#         context=super(single_medicine, self).get_context_data(**kwargs)
#         id1=self.request.GET['id']
#         view_medicine = Medicine.objects.get(id=id1)
#         context = {
#             'medicine':view_medicine
#         }
#         return context

