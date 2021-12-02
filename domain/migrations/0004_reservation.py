# Generated by Django 3.2.9 on 2021-12-02 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_delete_reservation'),
    ]

    operations = [
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
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.service')),
                ('subservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.subservice')),
            ],
            options={
                'unique_together': {('name', 'event', 'product', 'subservice')},
            },
        ),
    ]
