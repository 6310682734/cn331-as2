# Generated by Django 3.2.15 on 2022-09-20 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsubject', '0012_alter_enrollment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingsubject.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
