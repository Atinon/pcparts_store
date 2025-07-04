# Generated by Django 5.1.4 on 2025-01-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_orderitem_billing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('OTHER', 'Other'), ('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('MB', 'Motherboard'), ('SSD', 'Solid State Drive'), ('HDD', 'Hard Disk Drive'), ('PSU', 'Power Supply Unit'), ('CPU-COOLER', 'Cpu Cooler'), ('CASE', 'Case')], default='OTHER', max_length=100),
        ),
    ]
