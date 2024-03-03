# Generated by Django 4.2.6 on 2023-10-18 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_filme_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='atuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personagem', models.CharField(blank=True, max_length=100, null=True)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.filme')),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.membros')),
                ('tipoAtuar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoatuacao')),
            ],
        ),
    ]
