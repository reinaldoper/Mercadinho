# Generated by Django 2.2.5 on 2020-04-06 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20200406_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='compra',
        ),
    ]
