# Generated by Django 2.1.5 on 2019-01-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Photo_img',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]