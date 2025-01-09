output "workspace_name" {
  value = azurerm_machine_learning_workspace.workspace.name
}

output "workspace_identity_principal_id" {
  value = azurerm_machine_learning_workspace.workspace.primary_user_assigned_identity
}
