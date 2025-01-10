from azure.ai.ml import MLClient
from azure.ai.ml.entities import MarketplaceSubscription
from sdk.src.utils import AzureCredentialSingleton
from sdk.src.cli.config import ClientConfig
from sdk.src.resources.endpoint import create_endpoint
from typing import Any


class EndpointPipeline:

    def __init__(self):

        self.config = ClientConfig()
        self.ml_client = MLClient(
            credential = AzureCredentialSingleton().get_credential(),
            subscription_id = self.config.subscription_id
        )

    def _get_subscription(self, model_id: str) -> Any[MarketplaceSubscription, None]:
        
        subscriptions = self.ml_client.marketplace_subscriptions.list()
        for subscription in subscriptions:
            if model_id == subscription.model_id:
                return subscription
            
        return None

    def run(self, endpoint_name: str, model_id: str):

        subscription = self._get_subscription(model_id)
        if subscription:
            endpoint = create_endpoint(
                ml_client = self.ml_client,
                endpoint_name = endpoint_name,
                model_id = model_id
            )

            return endpoint