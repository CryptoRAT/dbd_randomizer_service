import pytest
import json
from perk.models import Perk
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_perk_creation():
    # Test creating a valid Perk object
    perk = Perk.objects.create(
        name="Dead Hard",
        owner="David King",
        type="Survivor",
        image_path="/path/to/deadhard.jpg"
    )

    assert perk.name == "Dead Hard"
    assert perk.owner == "David King"
    assert perk.type == "Survivor"
    assert perk.image_path == "/path/to/deadhard.jpg"


@pytest.mark.django_db
def test_perk_str_method():
    # Test that the __str__ method returns the name of the perk
    perk = Perk.objects.create(
        name="Borrowed Time",
        owner="Bill Overbeck",
        type="Survivor",
        image_path="/path/to/borrowedtime.jpg"
    )

    assert str(perk) == "Borrowed Time (Survivor, Bill Overbeck)"


@pytest.mark.django_db
def test_perk_to_json_with_internal_serializer():
    # Create a Perk instance
    perk = Perk.objects.create(
        name='Dead Hard',
        owner='David King',
        type='Survivor',
        image_path='/path/to/dead_hard.jpg'
    )

    # Get the JSON representation using the internal serializer
    perk_json = perk.to_json()

    # Convert the JSON string back to a Python list for comparison
    perk_list = json.loads(perk_json)

    # Verify that the JSON contains the correct structure and data
    assert len(perk_list) == 1  # Ensure it's a list with one element
    perk_data = perk_list[0]

    # Verify the model and pk metadata
    assert perk_data['model'] == 'perk.perk'
    assert perk_data['pk'] == perk.pk

    # Verify the fields
    fields = perk_data['fields']
    assert fields['name'] == 'Dead Hard'
    assert fields['owner'] == 'David King'
    assert fields['type'] == 'Survivor'
    assert fields['image_path'] == '/path/to/dead_hard.jpg'

@pytest.mark.django_db
def test_perk_invalid_type():
    # Test that creating a Perk with an invalid type raises a ValidationError
    perk = Perk(
        name="Hex: Ruin",
        owner="The Hag",
        type="InvalidType",  # Invalid type
        image_path="/path/to/hexruin.jpg"
    )

    with pytest.raises(ValidationError):
        perk.full_clean()  # Validate the model to trigger the validation error


@pytest.mark.django_db
def test_perk_valid_choices():
    # Test that valid choices for the 'type' field work correctly
    valid_types = ["Survivor", "Killer"]
    for valid_type in valid_types:
        perk = Perk.objects.create(
            name=f"Test {valid_type} Perk",
            owner="Test Owner",
            type=valid_type,
            image_path="/path/to/test.jpg"
        )
        assert perk.type == valid_type
