# Generated by Django 4.2.2 on 2023-06-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_categorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyFeaturesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
