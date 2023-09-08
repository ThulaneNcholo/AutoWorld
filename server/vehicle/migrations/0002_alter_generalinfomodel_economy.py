# Generated by Django 4.2.2 on 2023-06-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfomodel',
            name='economy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_economy', to='vehicle.economymodel'),
        ),
    ]