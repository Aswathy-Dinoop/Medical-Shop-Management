# Generated by Django 4.2.5 on 2023-10-07 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicalApp', '0004_pharmacy_pharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('phone', models.CharField(max_length=150, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('district', models.CharField(max_length=150, null=True)),
                ('password', models.CharField(max_length=150, null=True)),
                ('public_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
