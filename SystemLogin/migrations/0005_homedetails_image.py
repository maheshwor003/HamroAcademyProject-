# Generated by Django 4.0.3 on 2022-09-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemLogin', '0004_alter_homedetails_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedetails',
            name='image',
            field=models.ImageField(null=True, upload_to='static/'),
        ),
    ]