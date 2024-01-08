import os
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

CONTENT_TYPE = os.environ.get("Content-Type", "application/json")
ACCESS_CONTROL_ALLOW_HEADERS = os.environ.get(
    "Access-Control-Allow-Headers",
    "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
)
ACCESS_CONTROL_ALLOW_ORIGIN = os.environ.get("Access-Control-Allow-Origin", "*")
ACCESS_CONTROL_ALLOW_METHODS = os.environ.get(
    "Access-Control-Allow-Methods", "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT"
)


class Response:
    def __init__(
        self,
        status_code: int = 200,
        body: Dict = {},
        headers: Dict = {},
        is_base64_encoded: bool = False,
    ):
        self.status_code = status_code
        self.body = body
        self.headers = headers
        self.is_base64_encoded = is_base64_encoded

    @classmethod
    def ok(
        cls,
        body: Dict = {},
        headers: Dict = {},
        is_base64_encoded: bool = False,
    ):
        return cls(
            status_code=200,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    @classmethod
    def bad_request(
        cls,
        body: Dict = {},
        headers: Dict = {},
        is_base64_encoded: bool = False,
    ):
        return cls(
            status_code=400,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    @classmethod
    def unauthorised(
        cls,
        body: Dict = {},
        headers: Dict = {},
        is_base64_encoded: bool = False,
    ):
        return cls(
            status_code=401,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    @classmethod
    def internal_server_error(
        cls,
        body: Dict = {},
        headers: Dict = {},
        is_base64_encoded: bool = False,
    ):
        return cls(
            status_code=500,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    def update_headers(self, header: str, value: str) -> None:
        self.headers[header] = value

    def generate_response(self) -> Dict:
        headers = {
            **{
                "Content-Type": CONTENT_TYPE,
                "Access-Control-Allow-Headers": ACCESS_CONTROL_ALLOW_HEADERS,
                "Access-Control-Allow-Origin": ACCESS_CONTROL_ALLOW_ORIGIN,
                "Access-Control-Allow-Methods": ACCESS_CONTROL_ALLOW_METHODS,
            },
            **self.headers,
        }

        return {
            "isBase64Encoded": self.is_base64_encoded,
            "statusCode": self.status_code,
            "headers": headers,
            "body": json.dumps(self.body),
        }
