# Generated by Django 5.0.6 on 2024-07-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2app', '0008_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='../media'),
        ),
    ]
