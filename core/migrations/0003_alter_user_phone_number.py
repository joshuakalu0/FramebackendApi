# Generated by Django 3.2.12 on 2024-03-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]