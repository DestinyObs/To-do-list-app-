# Generated by Django 4.0.4 on 2022-06-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_listapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
