# Generated by Django 5.1.4 on 2024-12-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='status',
            field=models.CharField(choices=[('new', 'yangi'), ('Modeartion', 'Moderatsiya'), ('cod_verified', 'kod tasdiqlangan')], default='new', max_length=50),
        ),
    ]