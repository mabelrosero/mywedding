# Generated by Django 3.2.9 on 2021-12-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservice',
            name='products',
            field=models.ManyToManyField(to='domain.Product'),
        ),
        migrations.DeleteModel(
            name='SubServiceForEvent',
        ),
    ]
