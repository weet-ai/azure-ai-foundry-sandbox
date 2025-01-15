import os
from azure.ai.ml import MLClient
from sdk.src.utils import AzureCredentialSingleton

class ClientConfig(object):

    def __init__(self):

        self.subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        self.resource_group_name = os.getenv("AZURE_RESOURCE_GROUP_NAME")
        self.workspace_name = os.getenv("AZURE_AI_FOUNDRY_PROJECT_NAME")

class MLClientFacade(MLClient):

    def __init__(self, config: ClientConfig = None):

        if not config:
            config = ClientConfig()

        self.subscription_id = config.subscription_id
        self.resource_group_name =config.resource_group_name
        self.workspace_name = config.workspace_name

    def get_instance(self):

        client = MLClient(
            credential=AzureCredentialSingleton().get_credential(),
            subscription_id=self.subscription_id,
            resource_group_name=self.resource_group_name,
            workspace_name=self.workspace_name,
        )

        return client