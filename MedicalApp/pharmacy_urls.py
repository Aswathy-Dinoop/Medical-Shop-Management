from django.urls import path
from MedicalApp.pharmacy_views import index,Orders,single_medicine,View_Medicines_User,ViewReportTable,View_category
from MedicalApp import pharmacy_views

urlpatterns = [
    path('', index.as_view()),
    path('orderlist',Orders.as_view()),
    path('medicine',single_medicine.as_view()),
    path('shops',View_Medicines_User.as_view()),
    path('viewreport',ViewReportTable.as_view()),
    path('report12',pharmacy_views.reportview,name="report"),
    path('View_category',View_category.as_view())
    # path('remove',Remove.as_view()),
    # path('CartView',CartView.as_view()),
    # path('checkout',checkout.as_view()),
    # path('Thankyouforbooking',Thankyou.as_view()),
    # path('add_fb',Feedback.as_view()),
    # # path('rejectshop',RejectShop.as_view())

    # # path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'pharmacy','pharmacy'