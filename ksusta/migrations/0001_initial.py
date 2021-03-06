# Generated by Django 3.2.7 on 2021-09-24 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_faculty', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ksusta.facultie')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_title', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=6)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ksusta.department')),
            ],
        ),
    ]
