from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from MedicalApp.models import Medicine,Pharmacy,UserType,AddtoCart,Signup,Feedback,Assign,Category
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='Admin/index.html'

class Add_Medicines(TemplateView):
    template_name='Admin/add_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Medicines, self).get_context_data(**kwargs)
        pro = Category.objects.all()
        context['cate'] = pro
        return context
    def post(self, request, *args, **kwargs):
        name = request.POST['medi_name']
        price = request.POST['medi_price']
        image = request.FILES['medi_image']
        description = request.POST['medi_desc']
        direction = request.POST['medi_dir']
        warning = request.POST['medi_war']
        sideeffects = request.POST['medi_side']
        consumetype = request.POST['medi_type']
        quantity = request.POST['qty']

        ob=FileSystemStorage()   #create a object to load the image
        obj=ob.save(image.name, image)
        
        reg = Medicine ()# call the model
        reg.med_name=name
        reg.med_price=price
        reg.med_image=obj
        reg.med_desc=description
        reg.med_directionforuse=direction
        reg.med_warnings=warning
        reg.med_sideeffects=sideeffects
        reg.category_id=consumetype
        reg.med_totalquantity=quantity
        reg.save()
        return redirect('/admin')
        # return render(request, 'admin/index.html', {'message': "successfully added"})

class View_Medicines(TemplateView):
    template_name='admin/view_medicine.html'
    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context

class RejectMedicine(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Medicine.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})

class Add_Pharmacy(TemplateView):
    template_name="Admin/add_pharmacy.html"
    def post(self, request, *args, **kwargs):
        name = request.POST['pharmname']
        location = request.POST['pharm_loc']
        image = request.FILES['image']
        email = request.POST['Email']
        phone = request.POST['Phone_Number']
        password = request.POST['Phone_Number']
        
        ob=FileSystemStorage()   #create a object to load the image
        obj=ob.save(image.name, image)
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'Admin/add_pharmacy.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()
        
            reg = Pharmacy()# call the model
            reg.pharmacy=user
            reg.pharma_name=name
            reg.pharma_location=location
            reg.pharma_image=obj
            reg.pharma_email=email
            reg.pharma_phone=phone
            reg.password=password
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "pharmacy"
            usertype.save()
            return redirect('/admin')
            # return render(request, 'Admin/add_pharmacy.html', {'message': "Pharmacy successfully added"})

class View_Pharmacy(TemplateView):
    template_name='admin/view_pharmacy.html'
    def get_context_data(self, **kwargs):

        view_pharmacy = Pharmacy.objects.all()
        context = {
            'view_pharmacy':view_pharmacy
        }
        return context

class RejectShop(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Pharmacy.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})

class ConfirmOrder(TemplateView):
    template_name='Admin/confirm_order.html'
    def get_context_data(self, **kwargs):

        cart = AddtoCart.objects.filter(status="Added")
        context = {
            'cart_items':cart
        }
        return context

# class ApproveView(View):
#     def dispatch(self, request, *args, **kwargs):
#         id = request.GET['id']
#         user = AddtoCart.objects.get(pk=id)
#         user.status = 'approved'
#         user.save()
#         return render(request, 'Admin/index.html', {'message': " Order Approved"})

class Reject(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
    
class Manage_users(TemplateView):
    template_name="Admin/manage_users.html"
    def get_context_data(self, **kwargs):
        context = super(Manage_users, self).get_context_data(**kwargs)
        
        cart = AddtoCart.objects.all()

        
        context['cart'] = cart
       
        return context

class ApproveUser(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = AddtoCart.objects.get(pk=id)
        user.status = 'approved'
        user.save()
        return render(request, 'Admin/index.html', {'message': " Order Approved"})

class Rejectuser(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})

class fbview(TemplateView):
    template_name='Admin/fb_view.html'

    def get_context_data(self, **kwargs):
    
        
        view_fb = Feedback.objects.all()
        context = {
            'viewfb':view_fb
        }
        return context

class Assign_pharmacy(TemplateView):
    template_name='Admin/assign.html'

    def get_context_data(self, **kwargs):
        context= super(Assign_pharmacy,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        phar=Pharmacy.objects.all()
        cart=AddtoCart.objects.get(id=id)
        context['pharmacy']=phar
        context['cart']=cart
        return context
    def post(self, request, *args, **kwargs):
        id1 = request.POST['id1']
        pharmacy=request.POST['pharmacy']
        order=AddtoCart.objects.get(id=id1)
        qnty=order.quantity
        price=order.price
        order.status='Assigned'
        order.save()
        ca=Assign()
        ca.pharmacy_id=pharmacy
        ca.customer_id=order.public_user_id
        ca.medicine_id=order.medicine_id
        order.pharmacy_name_id=pharmacy
        ca.cart_id=order.id
        ca.quantity=qnty
        ca.price=price
        ca.status="Assigned"
        ca.save()
        return redirect('/admin')
        # return render(request, 'Admin/index.html',{'message':"Assigned"})

class Category_Add(TemplateView):
    template_name='Admin/category.html'
    def post(self, request, *args, **kwargs):
       category_name = request.POST['category']
       reg = Category ()# call the model
       reg.category_name=category_name
       reg.save()
       return redirect('/admin')
    #    return render(request, 'admin/index.html', {'message': "successfully added"})