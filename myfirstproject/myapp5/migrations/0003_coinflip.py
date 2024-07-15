# Generated by Django 5.0.6 on 2024-07-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0002_author_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinFlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_side', models.CharField(choices=[('heads', 'Орел'), ('tails', 'Решка')], max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]