# Generated by Django 4.1.3 on 2023-05-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Explorer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('awesome_font_logo', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=8000)),
            ],
        ),
    ]
