# Generated by Django 4.1 on 2022-09-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsubject', '0004_enrollment_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='username',
        ),
    ]
