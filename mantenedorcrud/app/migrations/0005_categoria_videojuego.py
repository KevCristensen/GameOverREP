# Generated by Django 3.2 on 2022-06-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_producto_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria_videojuego', models.CharField(max_length=50)),
            ],
        ),
    ]
