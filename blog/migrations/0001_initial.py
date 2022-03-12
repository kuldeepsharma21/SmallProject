# Generated by Django 4.0.2 on 2022-03-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
