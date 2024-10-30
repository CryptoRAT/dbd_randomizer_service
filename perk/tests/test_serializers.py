import pytest
from perk.serializers import PerkSerializer
from perk.models import Perk

@pytest.mark.django_db
def test_perk_serializer_valid_data():
    # Create a Perk instance
    perk = Perk(name="Dead Hard", owner="David King", type="Survivor", image_path="/path/to/dead_hard.jpg")

    # Initialize serializer with an instance
    serializer = PerkSerializer(instance=perk)

    # Check that the serialized data matches the model instance data
    assert serializer.data == {
        'name': 'Dead Hard',
        'owner': 'David King',
        'type': 'Survivor',
        'image_path': '/path/to/dead_hard.jpg'
    }

@pytest.mark.django_db
def test_perk_serializer_invalid_data():
    # Test serializer with invalid data (missing required fields)
    invalid_data = {'name': 'Dead Hard'}  # Missing 'owner', 'type', and 'image_path'

    serializer = PerkSerializer(data=invalid_data)

    # Serializer should not be valid
    assert not serializer.is_valid()

    # Check if the correct errors are raised for missing fields
    assert 'owner' in serializer.errors
    assert 'type' in serializer.errors
    assert 'image_path' in serializer.errors

@pytest.mark.django_db
def test_perk_serializer_create():
    # Test serializer for creating a new Perk object
    valid_data = {
        'name': 'Dead Hard',
        'owner': 'David King',
        'type': 'Survivor',
        'image_path': '/path/to/dead_hard.jpg'
    }

    # Create an instance using the serializer
    serializer = PerkSerializer(data=valid_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the object and check if it was created properly
    perk = serializer.save()
    assert perk.name == 'Dead Hard'
    assert perk.owner == 'David King'
    assert perk.type == 'Survivor'
    assert perk.image_path == '/path/to/dead_hard.jpg'

@pytest.mark.django_db
def test_perk_serializer_update():
    # Create an initial Perk instance
    perk = Perk.objects.create(name="Dead Hard", owner="David King", type="Survivor", image_path="/path/to/dead_hard.jpg")

    # Updated data
    update_data = {
        'name': 'Barbecue & Chili',
        'owner': 'Leatherface',
        'type': 'Killer',
        'image_path': '/path/to/bbq_chili.jpg'
    }

    # Initialize serializer with instance and updated data
    serializer = PerkSerializer(instance=perk, data=update_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the updated instance
    updated_perk = serializer.save()

    # Check if the instance is updated correctly
    assert updated_perk.name == 'Barbecue & Chili'
    assert updated_perk.owner == 'Leatherface'
    assert updated_perk.type == 'Killer'
    assert updated_perk.image_path == '/path/to/bbq_chili.jpg'
