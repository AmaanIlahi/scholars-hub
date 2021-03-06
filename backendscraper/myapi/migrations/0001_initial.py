# Generated by Django 3.2.3 on 2021-05-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=190)),
                ('salary', models.FloatField(null=True)),
                ('company', models.CharField(max_length=190, null=True)),
                ('date_posted', models.DateField(null=True)),
                ('last_date', models.DateField(null=True)),
            ],
        ),
    ]
