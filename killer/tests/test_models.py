import pytest
from killer.models import Killer


@pytest.mark.django_db
def test_killer_creation():
    # Create a new Killer object
    killer = Killer.objects.create(name="Freddy Krueger", image_path="/path/to/freddy.jpg")

    # Check that the killer was created and saved
    assert killer.name == "Freddy Krueger"
    assert killer.image_path == "/path/to/freddy.jpg"


@pytest.mark.django_db
def test_killer__self__method():
    # Create a new Killer object
    killer = Killer.objects.create(name="Michael Myers", image_path="/path/to/michael.jpg")

    # Check the ___self___ method
    assert str(killer) == "Michael Myers"
