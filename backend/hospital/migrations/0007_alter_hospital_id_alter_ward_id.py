# Generated by Django 4.1.4 on 2023-02-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_alter_hospital_id_alter_ward_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ward',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
