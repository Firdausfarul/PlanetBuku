# Generated by Django 4.2.6 on 2023-10-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
