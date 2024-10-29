import pytest
from survivor.serializers import SurvivorSerializer
from survivor.models import Survivor

@pytest.mark.django_db
def test_survivor_serializer_valid_data():
    # Create a Survivor instance
    survivor = Survivor(name="Dwight Fairfield", image_path="/path/to/dwight.jpg")

    # Initialize serializer with an instance
    serializer = SurvivorSerializer(instance=survivor)

    # Check that the serialized data matches the model instance data
    assert serializer.data == {
        'name': 'Dwight Fairfield',
        'image_path': '/path/to/dwight.jpg'
    }

@pytest.mark.django_db
def test_survivor_serializer_invalid_data():
    # Test serializer with invalid data (missing 'image_path')
    invalid_data = {'name': 'Dwight Fairfield'}

    serializer = SurvivorSerializer(data=invalid_data)

    # Serializer should not be valid
    assert not serializer.is_valid()

    # Check if the correct error is raised for missing fields
    assert 'image_path' in serializer.errors

@pytest.mark.django_db
def test_survivor_serializer_create():
    # Test serializer for creating a new Survivor object
    valid_data = {
        'name': 'Dwight Fairfield',
        'image_path': '/path/to/dwight.jpg'
    }

    # Create an instance using the serializer
    serializer = SurvivorSerializer(data=valid_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the object and check if it was created properly
    survivor = serializer.save()
    assert survivor.name == 'Dwight Fairfield'
    assert survivor.image_path == '/path/to/dwight.jpg'

@pytest.mark.django_db
def test_survivor_serializer_update():
    # Create an initial Survivor instance
    survivor = Survivor.objects.create(name="Dwight Fairfield", image_path="/path/to/dwight.jpg")

    # Updated data
    update_data = {
        'name': 'Meg Thomas',
        'image_path': '/path/to/meg.jpg'
    }

    # Initialize serializer with instance and updated data
    serializer = SurvivorSerializer(instance=survivor, data=update_data)

    # Check that the data is valid
    assert serializer.is_valid()

    # Save the updated instance
    updated_survivor = serializer.save()

    # Check if the instance is updated correctly
    assert updated_survivor.name == 'Meg Thomas'
    assert updated_survivor.image_path == '/path/to/meg.jpg'
