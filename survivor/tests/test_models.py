import pytest
import json
from survivor.models import Survivor

@pytest.mark.django_db
def test_survivor_creation():
    # Create a Survivor instance
    survivor = Survivor.objects.create(name="Dwight Fairfield", image_path="/path/to/dwight.jpg")

    # Check that the Survivor was created correctly
    assert survivor.name == "Dwight Fairfield"
    assert survivor.image_path == "/path/to/dwight.jpg"

@pytest.mark.django_db
def test_survivor_str_method():
    # Create a Survivor instance
    survivor = Survivor.objects.create(name="Dwight Fairfield", image_path="/path/to/dwight.jpg")

    # Check the __str__ method
    assert str(survivor) == "Dwight Fairfield (/path/to/dwight.jpg)"

@pytest.mark.django_db
def test_survivor_to_json_with_internal_serializer():
    # Create a Survivor instance
    survivor = Survivor.objects.create(
        name='Dwight Fairfield',
        image_path='/path/to/dwight.jpg'
    )

    # Get the JSON representation using the internal serializer
    survivor_json = survivor.to_json()

    # Convert the JSON string back to a Python list for comparison
    survivor_list = json.loads(survivor_json)

    # Verify that the JSON contains the correct structure and data
    assert len(survivor_list) == 1  # Ensure it's a list with one element
    survivor_data = survivor_list[0]

    # Verify the model and pk metadata
    assert survivor_data['model'] == 'survivor.survivor'  # Should be app_name.model_name
    assert survivor_data['pk'] == survivor.pk

    # Verify the fields
    fields = survivor_data['fields']
    assert fields['name'] == 'Dwight Fairfield'
    assert fields['image_path'] == '/path/to/dwight.jpg'
