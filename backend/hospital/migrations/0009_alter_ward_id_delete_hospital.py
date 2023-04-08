# Generated by Django 4.1.7 on 2023-04-07 11:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_appointment_hospital'),
        ('user', '0040_remove_hospitalstaff_hospital'),
        ('hospital', '0008_remove_ward_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]