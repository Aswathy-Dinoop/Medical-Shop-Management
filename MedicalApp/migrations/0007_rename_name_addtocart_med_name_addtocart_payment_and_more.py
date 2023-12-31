# Generated by Django 4.2.5 on 2023-10-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0006_pharmacy_register_addtocart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='name',
            new_name='med_name',
        ),
        migrations.AddField(
            model_name='addtocart',
            name='payment',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='status',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
