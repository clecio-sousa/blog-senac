# Generated by Django 3.0.5 on 2020-06-20 15:25

import datetime
from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 20, 12, 25, 0, 369860)),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 20, 12, 25, 0, 369860)),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, max_length=180, null=True, upload_to=website.models.upload_path),
        ),
    ]
