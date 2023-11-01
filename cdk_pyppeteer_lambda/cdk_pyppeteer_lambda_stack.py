from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_lambda_python as python_lambda
)

class CdkPyppeteerLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        lambda_function = python_lambda.PythonFunction(
            self, 'PyppeteerLambda',
            entry='lambda_function',
            handler='lambda_handler.lambda_handler',
            runtime=_lambda.Runtime.PYTHON_3_9
        )
