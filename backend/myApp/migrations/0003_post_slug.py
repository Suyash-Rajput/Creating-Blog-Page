# Generated by Django 5.0.4 on 2024-04-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_comment_text_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]