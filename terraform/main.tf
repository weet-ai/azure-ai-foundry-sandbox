provider "azurerm" {
  features {}

  # Explicitly set the subscription ID
  subscription_id = var.subscription_id
}

# Fetch the current Azure account details
data "azurerm_client_config" "current" {}

# Derive resource names based on the naming convention
locals {
  resource_group_name   = "${var.base_name}-${var.location}03"
  workspace_name        = "workspace03${replace(var.location, "-", "")}"
  keyvault_name         = "af03kv${replace(var.location, "-", "")}"
  storage_account_name  =  "aifoundrysaswc0301"
  app_insights_name     = "${var.base_name}-ai-${var.location}03"
}

# Deploy Resource Group
module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = local.resource_group_name
  location            = var.location
}

# Deploy User Assigned Managed Identity
module "uami" {
  source              = "./modules/user_assigned_identity"
  identity_name       = "${var.base_name}-uami-${var.location}03"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
}

# Deploy Key Vault
module "keyvault" {
  source              = "./modules/keyvault"
  keyvault_name       = local.keyvault_name
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
}

# Deploy Storage Account
module "storage_account" {
  source               = "./modules/storage_account"
  storage_account_name = local.storage_account_name
  resource_group_name  = module.resource_group.resource_group_name
  location             = module.resource_group.location
}

# Deploy Application Insights
module "application_insights" {
  source              = "./modules/application_insights"
  app_insights_name   = local.app_insights_name
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
}

module "role_assignment_uami" {
  source                          = "./modules/role_assignment_uami"
  scope                           = module.keyvault.id
  principal_id                    = module.uami.principal_id
}

# Deploy Azure AI Foundry Workspace
module "ai_foundry_workspace" {
  source              = "./modules/ai_foundry_workspace"
  workspace_name      = local.workspace_name
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  uami_id             = module.uami.id
  keyvault_id         = module.keyvault.id
  storage_account_id  = module.storage_account.id
  app_insights_id     = module.application_insights.id
  depends_on          = [module.uami, module.keyvault, module.role_assignment_uami]
}
