# Generated by Django 2.2.5 on 2020-04-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercado',
            name='datacompra',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mercado',
            name='itens',
            field=models.CharField(blank=True, choices=[('F', 'Frango'), ('M', 'Maionese'), ('C', 'Carne'), ('T', 'Tomate'), ('A', 'Arroz'), ('FE', 'Feijão'), ('FR', 'Frios'), ('B', 'Bebidas'), ('N', 'Nenhuma das opções')], default='N', max_length=255),
        ),
    ]
