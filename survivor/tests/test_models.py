import pytest
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
    assert str(survivor) == "Dwight Fairfield"
