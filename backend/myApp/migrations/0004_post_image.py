# Generated by Django 5.0.4 on 2024-04-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='1_tCLgoTtePAdJhGRImx-B-g.jpg', upload_to='blog'),
        ),
    ]
