from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def invalidate_property_cache(sender, **kwargs):
    """
    Invalide le cache 'all_properties' après création, modification ou suppression.
    """
    cache.delete('all_properties')
