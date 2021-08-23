# Generated by Django 3.2.5 on 2021-08-20 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replie',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('reply', models.CharField(max_length=100)),
                ('for_comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
