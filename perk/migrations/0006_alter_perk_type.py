# Generated by Django 4.1.13 on 2024-12-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perk', '0005_add_killer_perk_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perk',
            name='type',
            field=models.CharField(choices=[('Survivor', 'Survivor'), ('Killer', 'Killer')], max_length=10),
        ),
    ]
