# Generated by Django 5.1.3 on 2024-12-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_customuser_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('seller', 'Seller'), ('buyer', 'User')], default='buyer', max_length=10),
        ),
    ]
