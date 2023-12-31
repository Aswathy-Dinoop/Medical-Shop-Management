# Generated by Django 4.2.5 on 2023-10-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0009_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=150, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalApp.addtocart')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalApp.signup')),
                ('pharmacy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalApp.pharmacy')),
            ],
        ),
        migrations.DeleteModel(
            name='Pharmacy_Register',
        ),
    ]
