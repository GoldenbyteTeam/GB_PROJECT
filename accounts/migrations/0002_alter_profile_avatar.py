# Generated by Django 4.1.3 on 2023-05-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_images/11_Avocato_Brushcato.jpg', upload_to='profile_images'),
        ),
    ]
