# Generated by Django 2.2 on 2019-06-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_auto_20190618_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('N', 'Normal')], max_length=1),
        ),
    ]