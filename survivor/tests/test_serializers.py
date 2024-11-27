import pytest
from perk.models import Perk
from perk.serializers import PerkSerializer
from rest_framework.exceptions import ValidationError


@pytest.mark.django_db
def test_perk_serializer_valid_data():
    # Create a valid data payload
    data = {
        'name': 'Dead Hard',
        'owner': 'David King',
        'type': 'Survivor',
        'image_path': '/path/to/dead_hard.jpg'
    }

    # Initialize the serializer with data
    serializer = PerkSerializer(data=data)

    # Ensure serializer is valid and data is correct
    assert serializer.is_valid()
    assert serializer.validated_data['name'] == 'Dead Hard'
    assert serializer.validated_data['owner'] == 'David King'
    assert serializer.validated_data['type'] == 'Survivor'
    assert serializer.validated_data['image_path'] == '/path/to/dead_hard.jpg'


@pytest.mark.django_db
def test_perk_serializer_invalid_data():
    # Create invalid data (missing 'image_path')
    data = {
        'name': 'Dead Hard',
        'owner': 'David King',
        'type': 'Survivor'
    }

    # Initialize the serializer with data
    serializer = PerkSerializer(data=data)

    # Ensure the serializer is not valid and raises validation error
    assert not serializer.is_valid()
    assert 'image_path' in serializer.errors


@pytest.mark.django_db
def test_perk_serializer_serialization():
    # Create a Perk instance
    perk = Perk.objects.create(
        name='Dead Hard',
        owner='David King',
        type='Survivor',
        image_path='/path/to/dead_hard.jpg'
    )

    # Serialize the Perk instance
    serializer = PerkSerializer(perk)

    # Check that serialized data matches the Perk instance
    data = serializer.data
    assert data['name'] == 'Dead Hard'
    assert data['owner'] == 'David King'
    assert data['type'] == 'Survivor'
    assert data['image_path'] == '/path/to/dead_hard.jpg'


@pytest.mark.django_db
def test_perk_serializer_update():
    # Create a Perk instance
    perk = Perk.objects.create(
        name='Dead Hard',
        owner='David King',
        type='Survivor',
        image_path='/path/to/dead_hard.jpg'
    )

    # Create updated data
    updated_data = {
        'name': 'Borrowed Time',
        'owner': 'Bill Overbeck',
        'type': 'Survivor',
        'image_path': '/path/to/borrowed_time.jpg'
    }

    # Initialize the serializer with instance and updated data
    serializer = PerkSerializer(perk, data=updated_data)

    # Ensure the serializer is valid
    assert serializer.is_valid()

    # Update the Perk instance with the new data
    serializer.save()

    # Check that the instance was updated correctly
    updated_perk = Perk.objects.get(id=perk.id)
    assert updated_perk.name == 'Borrowed Time'
    assert updated_perk.owner == 'Bill Overbeck'
    assert updated_perk.type == 'Survivor'
    assert updated_perk.image_path == '/path/to/borrowed_time.jpg'


@pytest.mark.django_db
def test_perk_serializer_validation_owner_length():
    # Create invalid data where 'owner' is too short
    data = {
        'name': 'Dead Hard',
        'owner': 'Bo',  # Too short based on custom validation rule
        'type': 'Survivor',
        'image_path': '/path/to/dead_hard.jpg'
    }

    # Initialize the serializer with data
    serializer = PerkSerializer(data=data)

    # Ensure the serializer is not valid and raises validation error
    assert not serializer.is_valid()
    assert 'owner' in serializer.errors
    assert serializer.errors['owner'][0] == 'Owner name must be at least 3 characters long.'
