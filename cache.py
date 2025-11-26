# cache.py
import json
from pathlib import Path
from datetime import datetime, timedelta

CACHE_DIR = Path("data")
CACHE_DIR.mkdir(exist_ok=True)

TTL_MINUTES = 30

def _cache_file_for(key: str) -> Path:
    safe_key = key.lower().replace(" ", "_")
    return CACHE_DIR / f"{safe_key}_cache.json"


def load_cache(key: str):
    cache_file = _cache_file_for(key)

    if not cache_file.exists():
        return None, None  # no previous data

    with cache_file.open() as f:
        data = json.load(f)

    ts = datetime.fromisoformat(data["timestamp"])
    if datetime.now() - ts > timedelta(minutes=TTL_MINUTES):
        return None, data.get("payload")  # return previous to compare

    return data["payload"], data.get("previous")  # payload AND previous temp


def save_cache(key: str, payload):
    cache_file = _cache_file_for(key)
    CACHE_DIR.mkdir(exist_ok=True)

    # store previous temperature trend value
    previous_temp = payload.get("temperature")

    cache_file.write_text(json.dumps({
        "timestamp": datetime.now().isoformat(),
        "payload": payload,
        "previous": previous_temp
    }, indent=2))
