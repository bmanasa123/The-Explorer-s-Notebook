# Generated by Django 4.0.5 on 2022-06-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main_app', '0007_remove_travel_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.CharField(blank=True, default='../static/images/no-image.png', max_length=2000, null=True),
        ),
    ]
