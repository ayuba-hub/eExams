# Generated by Django 3.2.7 on 2021-09-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('exam', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile'),
        ),
    ]
