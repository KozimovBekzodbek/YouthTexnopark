# Generated by Django 5.0.4 on 2024-10-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_registration_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]