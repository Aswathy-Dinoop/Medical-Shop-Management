from django.urls import path
from MedicalApp.admin_views import index,Manage_users,ApproveUser,Assign_pharmacy,Rejectuser,fbview,Add_Medicines,Reject,ConfirmOrder,View_Medicines,RejectMedicine,Add_Pharmacy,View_Pharmacy,RejectShop,Category_Add

urlpatterns = [
    path('', index.as_view()),
    path('Add_Medicines',Add_Medicines.as_view()),
    path('View_Medicines',View_Medicines.as_view()),
    path('reject',RejectMedicine.as_view()),
    path('Add_Pharmacy',Add_Pharmacy.as_view()),
    path('View_Pharmacy',View_Pharmacy.as_view()),
    path('rejectshop',RejectShop.as_view()),
    path('confirmorder', ConfirmOrder.as_view()),
    #path('approve',ApproveView.as_view()),
    path('Reject',Reject.as_view()),
    path('Manage_users',Manage_users.as_view()),
    path('ApproveUser',ApproveUser.as_view()),
    path('Rejectuser',Rejectuser.as_view()),
    path('Feedback_view',fbview.as_view()),
    path('Assign_pharmacy',Assign_pharmacy.as_view()),
    path('Category_Add',Category_Add.as_view())


]

def urls():
    return urlpatterns, 'admin','admin'