from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Get all Property objects from Redis cache or DB if not cached.
    Cache the result for 1 hour.
    """
    all_properties = cache.get('all_properties')
    if all_properties is None:
        all_properties = list(Property.objects.all().values())
        cache.set('all_properties', all_properties, timeout=3600)  # 1h = 3600 sec
    return all_properties
