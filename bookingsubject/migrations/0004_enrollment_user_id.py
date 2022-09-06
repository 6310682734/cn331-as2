# Generated by Django 3.2.15 on 2022-09-06 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookingsubject', '0003_alter_enrollment_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
