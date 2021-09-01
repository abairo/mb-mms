# Generated by Django 3.2.6 on 2021-09-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=6)),
                ('timestamp', models.DateTimeField()),
                ('mms_20', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mms_50', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mms_200', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]