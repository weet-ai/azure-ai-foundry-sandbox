from azure.ai.ml import MLClient
from azure.ai.ml.entities import MarketplaceSubscription
import logging


logging.basicConfig(level="DEBUG")


def create_model_subscription(
    ml_client: MLClient,
    model_id: str,
    subscription_name: str,
    subscription_id: str,
    resource_group_name: str,
    workspace_name: str,
):

    marketplace_subscription = MarketplaceSubscription(
        model_id=model_id,
        name=subscription_name,
    )

    marketplace_subscription = (
        ml_client.marketplace_subscriptions.begin_create_or_update(
            marketplace_subscription
        )
    ).result()

    return marketplace_subscription
