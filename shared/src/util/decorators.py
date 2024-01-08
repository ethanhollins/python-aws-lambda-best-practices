import json
import logging
import traceback
from typing import Callable, Dict, Any
from functools import wraps
from typing import Dict, Callable, Any
from attrs import Attribute
from cattrs import structure
import jsonschema.exceptions
from jsonschema import validate
from util import get_schema
from apigw import Response


logger = logging.getLogger(__name__)


def structure_input(event_class: Attribute) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(event: Dict, ctx: Dict) -> Any:
            input_event = structure(event, event_class)
            return func(input_event, ctx)

        return wrapper

    return outer


def validate_json_schema(name: str) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(event, ctx) -> Any:
            logger.debug("validate_json_schema: %s", json.dumps(event, indent=2))
            schema = get_schema(name)
            try:
                validate(instance=event, schema=schema)
            except jsonschema.exceptions.ValidationError:
                logger.error(traceback.format_exc())
                return Response.bad_request(
                    body={"error": "Unable to parse body request"}
                ).generate_response()

            return func(event, ctx)

        return wrapper

    return outer
