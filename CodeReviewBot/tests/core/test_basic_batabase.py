import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_elementary_db():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1
