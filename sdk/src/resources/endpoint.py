from azure.ai.ml.entities import ServerlessEndpoint
from azure.ai.ml import MLClient


def create_endpoint(
    ml_client: MLClient,
    endpoint_name: str,
    model_id: str
):

    serverless_endpoint = ServerlessEndpoint(
        name=endpoint_name,
        model_id=model_id
    )

    created_endpoint = ml_client.serverless_endpoints.begin_create_or_update(
        serverless_endpoint
    ).result()

    return created_endpoint