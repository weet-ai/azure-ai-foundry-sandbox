# Fetch subscription and client details
data "azurerm_subscription" "primary" {}
data "azurerm_client_config" "current" {}

# Create a custom role definition
resource "azurerm_role_definition" "custom_role" {
  name               = "CustomKeyVaultReaderRole"
  role_definition_id = uuid() # Automatically generate a unique ID for the role definition
  scope              = var.scope

  permissions {
    actions = [
      "Microsoft.KeyVault/vaults/read"
    ]
    not_actions = []
  }

  assignable_scopes = [
    var.scope
  ]
}

# Assign the custom role to the UAMI
resource "azurerm_role_assignment" "keyvault_uami_role_assignment" {
  name               = uuid() # Automatically generate a unique ID for the role assignment
  scope              = var.scope
  role_definition_id = azurerm_role_definition.custom_role.role_definition_resource_id
  principal_id       = var.principal_id
}
