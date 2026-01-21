import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def save_to_json(hierarchy, path: str):
    logger.info(f"Saving hierarchy to {path}")

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(hierarchy, f, ensure_ascii=False, indent=2)

    logger.info("Save complete")