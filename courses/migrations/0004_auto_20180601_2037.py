# Generated by Django 2.0.4 on 2018-06-01 20:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20180426_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pendente'), (0, 'Aprovado'), (0, 'Cancelado')], default=0, verbose_name='Situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(on_delete=True, related_name='enrollments', to='courses.Course', verbose_name='Curso')),
                ('user', models.ForeignKey(on_delete=True, related_name='enrollments', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('user', 'course')},
        ),
    ]
