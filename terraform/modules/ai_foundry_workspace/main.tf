resource "azurerm_machine_learning_workspace" "workspace" {
  name                = var.workspace_name
  resource_group_name = var.resource_group_name
  location            = var.location

  sku_name = "Basic"

  identity {
    type = "UserAssigned"
    identity_ids = [var.uami_id]
  }

  primary_user_assigned_identity = var.uami_id

  storage_account_id      = var.storage_account_id
  key_vault_id            = var.keyvault_id
  application_insights_id = var.app_insights_id
}
