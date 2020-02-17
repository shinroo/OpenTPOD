# Generated by Django 2.2.10 on 2020-02-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_detector', '0009_auto_20191124_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detector',
            name='status',
            field=models.CharField(blank=True, choices=[('created', 'CREATED'), ('training', 'TRAINING'), ('trained', 'TRAINED'), ('error', 'ERRORED')], default='created', max_length=32, null=True),
        ),
    ]
