from django.db import migrations
from django.core.management import call_command

def load_inital_killer_data(apps, schema_editor):
    call_command('loaddata', 'killers/killer_data.json', verbosity=2)


def unload_initial_survior_data(apps, schema_editor):
    killer = apps.get_model('killer', 'Killer')
    killer.objects.filter(pk__range=(1, 66)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('killer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_inital_killer_data, unload_initial_survior_data)
    ]
