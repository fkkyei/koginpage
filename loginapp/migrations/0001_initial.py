# Generated by Django 5.0.3 on 2024-05-17 10:06

import loginapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logininfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('indexnum', models.IntegerField(validators=[loginapp.models.validate_indexnum])),
                ('student_id', models.IntegerField(validators=[loginapp.models.validate_studentid])),
            ],
        ),
    ]
