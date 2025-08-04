from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

["if total_requests > 0 else 0"]
["logger.error"]

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Récupère les statistiques Redis : hits, misses et ratio de succès du cache.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses

    hit_ratio = (hits / total) if total > 0 else 0.0

    logger.info(f"Redis Cache Metrics — Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2%}")

    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 4),
    }


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
