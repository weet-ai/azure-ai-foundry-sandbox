from src.utils import AzureCredentialSingleton
from azure.ai.ml import MLClient
from azure.ai.ml.entities import MarketplaceSubscription
import logging

logging.basicConfig(level = "DEBUG")

def create_model_subscription(
    model_id: str,
    subscription_name: str,
    subscription_id: str,
    resource_group_name: str,
    workspace_name: str
):

    client = MLClient(
        credential=AzureCredentialSingleton().get_credential(),
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        workspace_name=workspace_name
    )

    marketplace_subscription = MarketplaceSubscription(
        model_id=model_id,
        name=subscription_name,
    )

    marketplace_subscription = (
        client
        .marketplace_subscriptions
        .begin_create_or_update(marketplace_subscription)
    ).result()