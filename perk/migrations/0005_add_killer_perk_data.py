from django.db import migrations, models
from django.core.management import call_command

def load_inital_killer_perk_data(apps, schema_editor):
    call_command('loaddata', 'perks/killer_perk_data.json', verbosity=2)


def unload_initial_killer_perk_data(apps, schema_editor):
    perk = apps.get_model('perk', 'Perk')
    perk.objects.filter(pk__range=(1, 66)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('perk', '0001_initial'),
        ('perk', '0004_alter_perk_type')
    ]

    operations = [
        migrations.RunPython(load_inital_killer_perk_data, unload_initial_killer_perk_data)
    ]
