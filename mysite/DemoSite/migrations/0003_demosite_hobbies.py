# Generated by Django 3.2.5 on 2021-08-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoSite', '0002_alter_demosite_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='demosite',
            name='hobbies',
            field=models.CharField(default='', max_length=500),
        ),
    ]