#!/usr/bin/env python3
import aws_cdk as cdk
from omegaconf import OmegaConf
from narrator.narrator_stack import NarratorStack


app = cdk.App()

config = app.node.try_get_context("config")
conf = OmegaConf.load("config/{0}/config.yaml".format(config))

NarratorStack(
    app,
    "examples-narrator-stack",
    env=cdk.Environment(region=conf.aws.region, account=conf.aws.account_id),
    conf=conf,
)

app.synth()
