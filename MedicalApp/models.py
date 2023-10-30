from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)

class Category(models.Model):
    category_name= models.CharField(max_length=150,null=True)

class Medicine(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    med_name = models.CharField(max_length=150,null=True)
    med_image = models.ImageField(upload_to='media/',null=True)
    med_desc = models.CharField(max_length=1550,null=True)
    med_price = models.CharField(max_length=50,null=True)
    med_totalquantity = models.CharField(max_length=50,null=True)
    med_directionforuse = models.CharField(max_length=550,null=True)
    med_sideeffects = models.CharField(max_length=550,null=True)
    med_warnings = models.CharField(max_length=550,null=True)
    # med_consumetype = models.CharField(max_length=150,null=True)

class Pharmacy(models.Model):
    pharmacy=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pharma_name = models.CharField(max_length=200,null=True)
    pharma_location = models.CharField(max_length=200,null=True)
    pharma_phone = models.CharField(max_length=200,null=True)
    pharma_email =models.EmailField(max_length=200,null=True)
    pharma_image = models.ImageField(upload_to='media/',null=True)
    password = models.CharField(max_length=150,null=True)

class Signup(models.Model):
    public_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=150,null=True)
    phone=models.CharField(max_length=150,null=True)
    address=models.CharField(max_length=150,null=True)
    district=models.CharField(max_length=150,null=True)
    password = models.CharField(max_length=150,null=True)

# class Pharmacy_Register(models.Model):
#     pharmacy_staff=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     name=models.CharField(max_length=150,null=True)
#     email=models.CharField(max_length=150,null=True)
#     phone=models.CharField(max_length=150,null=True)
#     address=models.CharField(max_length=150,null=True)
#     district=models.CharField(max_length=150,null=True)
#     password = models.CharField(max_length=150,null=True)

class AddtoCart(models.Model):
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    pharmacy_name=models.ForeignKey(Pharmacy,on_delete=models.CASCADE,null=True)

    public_user=models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/',null=True)
    med_name=models.CharField(max_length=150,null=True)
    price=models.CharField(max_length=150,null=True)
    quantity=models.CharField(max_length=150,null=True)
    status=models.CharField(max_length=150,null=True)
    payment=models.CharField(max_length=150,null=True)

class Feedback(models.Model):
    user=models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=150,null=True)
    service=models.CharField(max_length=150,null=True)

class Assign(models.Model):
    cart=models.ForeignKey(AddtoCart,on_delete=models.CASCADE,null=True)
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    pharmacy=models.ForeignKey(Pharmacy,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=150,null=True)
    quantity=models.CharField(max_length=150,null=True)
    price=models.CharField(max_length=150,null=True)


