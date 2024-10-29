import pytest
from killer.serializers import KillerSerializer
from killer.models import Killer

@pytest.mark.django_db
def test_killer_serializer_valid_data():
    # Create a Killer instance
    killer = Killer(name="Freddy Krueger", image_path="/path/to/freddy.jpg")

    # Initialize serializer with an instance
    serializer = KillerSerializer(instance=killer)

    # Check that the serialized data matches the model instance data
    assert serializer.data == {
        'name': 'Freddy Krueger',
        'image_path': '/path/to/freddy.jpg'
    }

@pytest.mark.django_db
def test_killer_serializer_invalid_data():
    # Test serializer with missing required fields
    invalid_data = {'name': ''}  # Missing 'image_path'

    serializer = KillerSerializer(data=invalid_data)

    # Serializer should not be valid
    assert not serializer.is_valid()

    # Check if the correct error is raised for the missing 'image_path'
    assert 'image_path' in serializer.errors
    assert 'name' in serializer.errors  # Name is blank

@pytest.mark.django_db
def test_killer_serializer_create():
    # Test serializer for creating a new Killer object
    valid_data = {
        'name': 'Michael Myers',
        'image_path': '/path/to/michael.jpg'
    }

    # Create an instance using the serializer
    serializer = KillerSerializer(data=valid_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the object and check if it was created properly
    killer = serializer.save()
    assert killer.name == 'Michael Myers'
    assert killer.image_path == '/path/to/michael.jpg'

@pytest.mark.django_db
def test_killer_serializer_update():
    # Create an initial Killer instance
    killer = Killer.objects.create(name="Freddy Krueger", image_path="/path/to/freddy.jpg")

    # Updated data
    update_data = {
        'name': 'Jason Voorhees',
        'image_path': '/path/to/jason.jpg'
    }

    # Initialize serializer with instance and updated data
    serializer = KillerSerializer(instance=killer, data=update_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the updated instance
    updated_killer = serializer.save()

    # Check if the instance is updated correctly
    assert updated_killer.name == 'Jason Voorhees'
    assert updated_killer.image_path == '/path/to/jason.jpg'
