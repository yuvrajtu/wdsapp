# Generated by Django 2.1 on 2018-10-22 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20181021_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstockdisplay',
            name='TeamId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserProfileInfo'),
        ),
    ]
