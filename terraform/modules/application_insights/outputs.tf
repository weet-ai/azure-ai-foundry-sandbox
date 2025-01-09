output "id" {
  value = azurerm_application_insights.app_insights.id
}

output "workspace_id" {
  value = azurerm_log_analytics_workspace.log_analytics.id
}
