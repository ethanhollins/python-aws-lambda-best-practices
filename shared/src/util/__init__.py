import json
import pathlib
import logging
from functools import wraps
from typing import Dict, Callable, Any


logger = logging.getLogger(__name__)


def get_schema(name: str) -> Dict:
    current_dir = pathlib.Path(name).parent.resolve()
    with open(f"{current_dir}/schema.json", "r", encoding="utf-8") as file:
        schema = json.load(file)
    return schema
