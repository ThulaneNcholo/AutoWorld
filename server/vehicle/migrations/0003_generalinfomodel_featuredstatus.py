# Generated by Django 4.2.2 on 2023-06-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_generalinfomodel_economy'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfomodel',
            name='featuredStatus',
            field=models.CharField(blank=True, default='Pending', max_length=200, null=True),
        ),
    ]
