# Generated by Django 5.0.4 on 2024-04-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]