# Generated by Django 4.0.5 on 2022-06-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic= False
    dependencies = [
        ('main_app', '0002_checking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='checking',
            options={'ordering': ['date']},
        ),
    ]