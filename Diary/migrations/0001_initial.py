# Generated by Django 3.1.2 on 2021-03-22 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Text', models.TextField()),
                ('Date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
