# Generated by Django 3.0.11 on 2020-12-23 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20201223_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personas',
            name='estado_civil',
        ),
        migrations.AddField(
            model_name='personas',
            name='estado_civil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.EstadoCivil'),
        ),
    ]
