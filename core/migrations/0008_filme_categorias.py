# Generated by Django 4.2.6 on 2023-10-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='categorias',
            field=models.ManyToManyField(to='core.categoria'),
        ),
    ]