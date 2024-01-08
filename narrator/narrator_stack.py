from typing import Any
from aws_cdk import (
    Stack,
)
from constructs import Construct


class NarratorStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, conf: Any = None, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
