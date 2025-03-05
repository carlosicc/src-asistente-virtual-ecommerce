class Config:
    # Stack name
    # Change this value if you want to create a new instance of the stack
    STACK_NAME = "StAppGenAIAssistantV01"
    
    # Put your own custom value here to prevent ALB to accept requests from
    # other clients that CloudFront. You can choose any random string.
    CUSTOM_HEADER_VALUE = "GenAIAssistant_v0.1.1"    
    
    # ID of Secrets Manager containing cognito parameters
    # When you delete a secret, you cannot create another one immediately
    # with the same name. Change this value if you destroy your stack and need
    # to recreate it with the same STACK_NAME.
    SECRETS_MANAGER_ID = f"{STACK_NAME}ParamCognitoSecret-v0_1"

    # AWS region in which you want to deploy the cdk stack
    DEPLOYMENT_REGION = "us-west-2"

    # Since Bedrock is not activated in X, we set this value
    BEDROCK_REGION = "us-west-2"
