# Generated by Django 3.2.15 on 2022-09-20 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsubject', '0013_auto_20220920_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsubject.subject', unique=True),
        ),
    ]
