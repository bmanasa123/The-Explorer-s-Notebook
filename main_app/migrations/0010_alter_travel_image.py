# Generated by Django 4.0.5 on 2022-06-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main_app', '0009_alter_travel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]
