# Generated by Django 2.0.6 on 2018-08-01 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180731_2355'),
        ('accounts', '0004_auto_20180601_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='endereco',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Endereco'),
        ),
    ]
