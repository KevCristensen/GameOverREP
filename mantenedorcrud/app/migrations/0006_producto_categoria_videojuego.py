# Generated by Django 3.2 on 2022-06-25 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_categoria_videojuego'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_videojuego',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.categoria_videojuego'),
        ),
    ]
