import pytest
import json
from killer.models import Killer


@pytest.mark.django_db
def test_killer_creation():
    # Create a new Killer object
    killer = Killer.objects.create(name="Freddy Krueger", image_path="/path/to/freddy.jpg")

    # Check that the killer was created and saved
    assert killer.name == "Freddy Krueger"
    assert killer.image_path == "/path/to/freddy.jpg"


@pytest.mark.django_db
def test_killer__str__method():
    # Create a new Killer object
    killer = Killer.objects.create(name="Michael Myers", image_path="/path/to/michael.jpg")

    # Check the ___self___ method
    assert str(killer) == "Michael Myers (/path/to/michael.jpg)"

@pytest.mark.django_db
def test_killer_to_json_with_internal_serializer():
    # Create a Killer instance
    killer = Killer.objects.create(
        name='Freddy Krueger',
        image_path='/path/to/freddy.jpg'
    )

    # Get the JSON representation using the internal serializer
    killer_json = killer.to_json()

    # Convert the JSON string back to a Python list for comparison
    killer_list = json.loads(killer_json)

    # Verify that the JSON contains the correct structure and data
    assert len(killer_list) == 1  # Ensure it's a list with one element
    killer_data = killer_list[0]

    # Verify the model and pk metadata
    assert killer_data['model'] == 'killer.killer'  # Should be app_name.model_name
    assert killer_data['pk'] == killer.pk

    # Verify the fields
    fields = killer_data['fields']
    assert fields['name'] == 'Freddy Krueger'
    assert fields['image_path'] == '/path/to/freddy.jpg'

