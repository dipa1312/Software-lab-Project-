# Generated by Django 4.2.5 on 2023-12-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_recruitment_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100)),
                ('courseid', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('classtime', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ExcelData',
        ),
        migrations.RemoveField(
            model_name='recruitment',
            name='file',
        ),
    ]
