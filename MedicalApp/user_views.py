from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from MedicalApp.models import Medicine,AddtoCart,Signup,Feedback,Assign
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='user/index.html'
    
    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context

class View_Medicines_User(TemplateView):
    template_name='user/shop.html'
    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context

class single_medicine(TemplateView):
    template_name='user/shop-single.html'
    def get_context_data(self, **kwargs):
        context=super(single_medicine, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view_medicine = Medicine.objects.get(id=id1)
        context = {
            'medicine':view_medicine
        }
        return context

class Add_Cart(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.POST['id']  #shop-single html pagil ninu eduthath type hidden line
        qty=request.POST['req_quantity']
        med=Medicine.objects.get(id=id)
        medi_name=med.med_name
        Tquantity=int(med.med_totalquantity)-int (qty)
        price=med.med_price
        total=int(qty)*int(price)
        med.med_totalquantity=int(med.med_totalquantity)-int (qty)
        med.save()
        re = Signup.objects.get(public_user_id=self.request.user.id)
        ca=AddtoCart()
        ca.medicine_id=id 
        ca.public_user_id=re.id
        ca.status = 'Added'
        ca.payment = 'NULL'
        ca.price=total
        ca.quantity=qty
        ca.med_name=medi_name
        # ca.Tquantity=Tquantity
        ca.save()       
        #return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})
        return redirect('/user')

class CartView(TemplateView):
    template_name="user/cart.html"
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)  
        user = Signup.objects.get(public_user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status='Added',public_user_id=user.id)
        sum=0
        for i in cart:
            sum=sum+int(i.price)

        context["totalvalue"] = sum

        context['cart'] = cart
        return context

class Remove(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        id2= request.GET['id2']
        cart= AddtoCart.objects.get(id=id)
        qty=cart.quantity
        med=Medicine.objects.get(id=id2)
        med.med_totalquantity=int(med.med_totalquantity)+int(qty)
        med.save()
        AddtoCart.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Item remove"})

class checkout(TemplateView):
    template_name='user/checkout.html'
    def get_context_data(self, **kwargs):
        context = super(checkout, self).get_context_data(**kwargs) 
        user = Signup.objects.get(public_user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status='Added',public_user_id=user.id)
        sum=0
        for i in cart:
            sum=sum+int(i.price)

        context["totalvalue"] = sum
        context['user'] = user
        context['booked_items'] = cart
        return context

      

class Thankyou(TemplateView):
    template_name ='user/thankyou.html'

class Fback(TemplateView):
    template_name='user/feedback.html'
    def post(self, request, *args, **kwargs):
        abc=Signup.objects.get(public_user_id=self.request.user.id)
        service = request.POST['service']
        message = request.POST['message']
       
        
        reg = Feedback()# call the model
        reg.message=message
        reg.service=service
        reg.user_id=abc.id
        reg.save()
       
        return redirect('/user', {'message': "Feedback Send"})

class StatusView(TemplateView):
    template_name="User/order_status.html"
    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)  
        user = Signup.objects.get(public_user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Accepted",public_user_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context

class Payment(TemplateView):
    template_name="User/payment.html"
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)  
        user = Signup.objects.get(public_user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Accepted",public_user_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context
    
class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        user = Signup.objects.get(public_user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Accepted",public_user_id=user.id)
        asg = Assign.objects.filter(status="Accepted",customer_id=user.id)
        print(cart)
        for i in cart:
            i.payment = 'paid'
            i.status = 'paid'
            i.save()
        for i in asg:
            i.status = 'paid'
            i.save()
        return render(request,'User/thanks.html',{'message':" payment Success"})

def demo(request):
    return render(request, 'index.html')