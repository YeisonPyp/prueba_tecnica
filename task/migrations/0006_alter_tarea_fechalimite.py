# Generated by Django 4.0 on 2023-04-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_persona_fechanacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechalimite',
            field=models.DateField(),
        ),
    ]
