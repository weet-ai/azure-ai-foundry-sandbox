"""CLI Entrypoints for Sandbox functionality."""

from sdk.src.cli.config import ClientConfig, MLClientFacade
import click
import logging

logging.basicConfig(level = "DEBUG")


@click.group()
def sandbox():
    click.echo("Azure AI Foundry Sandbox")
    pass

# Subscription group
@sandbox.group()
def subscription():
    """Manage subscriptions."""
    pass

@subscription.command("create")
@click.argument("model_id")
def create_subscription(model_id):
    """Create a subscription for the given MODEL_ID."""
    client = MLClientFacade()

# Endpoint group
@sandbox.group()
def endpoint():
    """Manage endpoints."""
    pass

@endpoint.command("create")
@click.argument("model_id")
def create_endpoint(model_id):
    """Create an endpoint for the given MODEL_ID."""
    click.echo(f"Endpoint created for model_id: {model_id}")

if __name__ == "__main__":
    sandbox()
