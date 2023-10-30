from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from MedicalApp.models import Assign,Pharmacy,AddtoCart,Medicine,Category
from django.contrib.auth.models import User
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


class index(TemplateView):
    def get_context_data(self, **kwargs):
        pro = Category.objects.all()

        context = {
            'pro':pro
        }
        return context

    template_name='pharmacy/index.html'

    def get_context_data(self, **kwargs):

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine
        }
        return context

class Orders(TemplateView):
    template_name='pharmacy/orderlist.html'
    def get_context_data(self, **kwargs):
        context = super(Orders, self).get_context_data(**kwargs)
        id1=Pharmacy.objects.get(pharmacy_id=self.request.user.id)
        assign=Assign.objects.filter(status="Assigned",pharmacy_id=id1)   
        context['asign']=assign
        return context
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        sta=request.POST['status']
        s=Assign.objects.get(id=id)
        s.status = sta
        s.save()
        c=AddtoCart.objects.get(id=s.cart_id)
        c.status = sta
        c.save()
        return redirect('/pharmacy')

class View_Medicines_User(TemplateView):
    template_name='pharmacy/shop.html'
    # def get_context_data(self, **kwargs):
    #     context = super(View_Medicines_User, self).get_context_data(**kwargs)
    #     pro = Category.objects.all()
    #     context['cate'] = pro
    #     return context
    def get_context_data(self, **kwargs):
        pro = Category.objects.all()

        view_medicine = Medicine.objects.all()
        context = {
            'view_medicine':view_medicine,
            'pro':pro
        }
        return context
    
class View_category(TemplateView):
    template_name='pharmacy/category.html'
    def get_context_data(self, **kwargs):
        context=super(View_category, self).get_context_data(**kwargs)
        cat_id=self.request.GET['catg_id']
        category = Category.objects.all()

        view_medicine = Medicine.objects.filter(category_id=cat_id)
        context = {
            'medicine':view_medicine,
            'category':category

        }
        return context

class single_medicine(TemplateView):
    template_name='pharmacy/shop-single.html'
    def get_context_data(self, **kwargs):
        context=super(single_medicine, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view_medicine = Medicine.objects.get(id=id1)
        context = {
            'medicine':view_medicine
        }
        return context

class ViewReportTable(TemplateView):
    template_name = "pharmacy/view_report.html"    
    def get_context_data(self, **kwargs):
        context = super(ViewReportTable, self).get_context_data(**kwargs)        
        med = Medicine.objects.all()
        context['medicine'] = med
        return context

def reportview(request):
    rm=Medicine.objects.all()
    template_path = 'pharmacy/report.html'
    context = {'rep': rm}
        # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="report.pdf"'
        # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

        # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response