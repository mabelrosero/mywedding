# Generated by Django 3.2.9 on 2021-12-01 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=9)),
                ('event_date', models.DateField()),
                ('guest', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.service')),
            ],
            options={
                'unique_together': {('name', 'service')},
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.TextField()),
                ('unit', models.TextField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.supplier')),
            ],
            options={
                'unique_together': {('name', 'supplier')},
            },
        ),
        migrations.CreateModel(
            name='SubServiceForEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.event')),
                ('subservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.subservice')),
            ],
            options={
                'unique_together': {('name', 'event', 'subservice')},
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('reservation_date', models.DateField(default='2021-11-25')),
                ('start_date', models.DateField(default='2021-11-25')),
                ('finish_date', models.DateField(default='2021-11-25')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.event')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.product')),
                ('subservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.subservice')),
            ],
            options={
                'unique_together': {('name', 'event', 'product', 'subservice')},
            },
        ),
    ]
