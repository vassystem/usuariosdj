# Generated by Django 3.0.8 on 2020-07-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='codregistro',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]
