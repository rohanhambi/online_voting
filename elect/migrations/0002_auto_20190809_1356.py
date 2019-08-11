# Generated by Django 2.2.4 on 2019-08-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30, null=True, unique=True)),
                ('nominatior', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='voters',
            name='DOB',
        ),
        migrations.AddField(
            model_name='voters',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='voters',
            name='aadhar',
            field=models.CharField(max_length=100, primary_key='True', serialize=False, unique=True),
        ),
    ]
