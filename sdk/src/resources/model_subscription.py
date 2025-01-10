from azure.ai.ml import MLClient
from azure.ai.ml.entities import MarketplaceSubscription
import logging
from typing import Iterable


logging.basicConfig(level="DEBUG")


def create_model_subscription(
    ml_client: MLClient,
    model_id: str,
    subscription_name: str
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


def get_model_subscription(
    ml_client: MLClient,
    model_id: str
):
    
    subscriptions: Iterable[MarketplaceSubscription] = ml_client.marketplace_subscriptions.list()
    for subscription in subscriptions:
        if model_id == subscription.model_id:
            return subscription
        
    return None