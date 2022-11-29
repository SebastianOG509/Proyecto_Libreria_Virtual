# Generated by Django 4.1.3 on 2022-11-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.CharField(choices=[('P', 'En prestamo'), ('D', 'Disponible'), ('N', 'No Disponible')], max_length=1),
        ),
    ]
