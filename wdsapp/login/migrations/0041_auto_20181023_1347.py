# Generated by Django 2.1 on 2018-10-23 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0040_auto_20181023_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstockdisplay',
            name='StockName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Stock'),
        ),
    ]
