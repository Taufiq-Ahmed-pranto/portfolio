# Generated by Django 3.1.7 on 2021-12-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('link', models.CharField(max_length=2000)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
    ]