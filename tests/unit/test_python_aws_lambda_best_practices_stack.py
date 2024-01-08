import aws_cdk as core
import aws_cdk.assertions as assertions

from python_aws_lambda_best_practices.python_aws_lambda_best_practices_stack import PythonAwsLambdaBestPracticesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_aws_lambda_best_practices/python_aws_lambda_best_practices_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonAwsLambdaBestPracticesStack(app, "python-aws-lambda-best-practices")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
