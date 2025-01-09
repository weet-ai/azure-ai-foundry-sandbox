resource "azurerm_role_assignment" "keyvault_workspace_assignment" {
  scope                = var.scope
  role_definition_name = "Key Vault Secrets User"
  principal_id         = var.workspace_identity_principal_id
}