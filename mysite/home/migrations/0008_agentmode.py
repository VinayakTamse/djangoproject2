# Generated by Django 3.2.5 on 2021-08-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_usermember_usermemberid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentMode',
            fields=[
                ('ag_id', models.AutoField(primary_key=True, serialize=False)),
                ('ag_name', models.CharField(max_length=20)),
                ('ag_phone', models.CharField(max_length=15)),
            ],
        ),
    ]