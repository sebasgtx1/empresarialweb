# Generated by Django 4.2.2 on 2023-07-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Social network'),
        ),
    ]
