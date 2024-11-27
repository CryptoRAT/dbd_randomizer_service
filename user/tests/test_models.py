import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
def test_create_user_with_email():
    # Valid user creation
    user = User.objects.create_user(email='testuser@example.com', password='testpassword', name='Test User')
    assert user.email == 'testuser@example.com'
    assert user.name == 'Test User'
    assert user.is_active
    assert not user.is_staff
    assert user.check_password('testpassword')  # Verify the password

@pytest.mark.django_db
def test_create_user_without_email():
    # Try creating a user without an email
    with pytest.raises(ValueError, match='The Email field must be set'):
        User.objects.create_user(email=None, password='testpassword', name='Test User')

@pytest.mark.django_db
def test_create_superuser():
    # Create a superuser
    superuser = User.objects.create_superuser(email='admin@example.com', password='adminpassword', name='Admin User')
    assert superuser.email == 'admin@example.com'
    assert superuser.is_staff
    assert superuser.is_superuser
    assert superuser.check_password('adminpassword')

@pytest.mark.django_db
def test_create_superuser_with_defaults():
    # Test that 'is_staff' and 'is_superuser' are set to True by default
    superuser = User.objects.create_superuser(email='admin@example.com', password='adminpassword', name='Admin User')
    assert superuser.is_staff is True
    assert superuser.is_superuser is True

@pytest.mark.django_db
def test_user_email_uniqueness():
    # Test email uniqueness constraint
    User.objects.create_user(email='unique@example.com', password='password', name='Unique User')
    with pytest.raises(IntegrityError):
        User.objects.create_user(email='unique@example.com', password='password', name='Another User')

@pytest.mark.django_db
def test_registered_user_str_method():
    user = User.objects.create_user(email='testuser@example.com', password='password', name='Test User')
    assert str(user) == 'testuser@example.com: Test User'
