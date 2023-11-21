from django.db import migrations
from django.core.management import call_command

def load_generic_perk_data(apps, schema_editor):
    call_command('loaddata', 'perks/generic_survivor_perk_data.json', verbosity=2)


def unload_generic_perk_data(apps, schema_editor):
    perk = apps.get_model('perk', 'Perk')
    perk.objects.filter(pk__range=(1, 66)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('perk', '0001_initial'),
        ('perk', '0002_add_perk_data')
    ]

    operations = [
        migrations.RunPython(load_generic_perk_data, unload_generic_perk_data)
    ]