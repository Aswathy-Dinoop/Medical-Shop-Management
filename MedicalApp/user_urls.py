from django.urls import path
from MedicalApp.user_views import index,single_medicine,Payment,chpayment,Fback,StatusView,checkout,Thankyou,CartView,View_Medicines_User,Add_Cart,Remove
urlpatterns = [
    path('', index.as_view()),
    path('medicine',single_medicine.as_view()),
    path('shops',View_Medicines_User.as_view()),
    path('AddtoCart',Add_Cart.as_view()),
    path('remove',Remove.as_view()),
    path('CartView',CartView.as_view()),
    path('checkout',checkout.as_view()),
    path('Thankyouforbooking',Thankyou.as_view()),
    path('add_fb',Fback.as_view()),
    path('orderstatus',StatusView.as_view()),
    path('payment',Payment.as_view()),
    path('chpayment',chpayment.as_view())

    # path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'user','user'