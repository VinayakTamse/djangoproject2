# Generated by Django 3.2.5 on 2021-08-02 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_usermember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermember',
            old_name='usermemberEmail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='usermember',
            old_name='usermemberName',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='usermember',
            name='usermemberId',
        ),
    ]
