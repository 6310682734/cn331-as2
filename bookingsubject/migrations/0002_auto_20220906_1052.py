# Generated by Django 3.2.15 on 2022-09-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsubject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('subject_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]