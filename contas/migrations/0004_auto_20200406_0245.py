# Generated by Django 2.2.5 on 2020-04-06 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20200406_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cliente',
            new_name='compra',
        ),
    ]
