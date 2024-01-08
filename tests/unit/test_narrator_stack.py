import aws_cdk as core
import aws_cdk.assertions as assertions
from narrator.narrator_stack import NarratorStack


def test_sqs_queue_created():
    app = core.App()
    stack = NarratorStack(app, "examples-narrator-stack")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
