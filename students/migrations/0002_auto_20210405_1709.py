# Generated by Django 3.1.5 on 2021-04-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
