# Generated by Django 5.1.3 on 2024-11-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.CharField(choices=[('admin', 'Admin'), ('cliente', 'Cliente')], max_length=10),
        ),
    ]
