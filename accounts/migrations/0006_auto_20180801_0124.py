# Generated by Django 2.0.6 on 2018-08-01 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='endereco',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, to='core.Endereco'),
        ),
    ]
