# Generated by Django 3.2.5 on 2021-08-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='blog_content',
            field=models.TextField(max_length=5000),
        ),
    ]
