import django
import pytest
from django.conf import settings

if not settings.configured:
    django.setup()

pytestmark = pytest.mark.django_db  
