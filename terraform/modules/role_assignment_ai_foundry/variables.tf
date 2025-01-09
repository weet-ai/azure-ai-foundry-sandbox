variable "scope" {
  description = "The scope at which the role will be assigned (e.g., a resource, resource group, or subscription)."
  type        = string
}

variable "workspace_identity_principal_id" {
  description = "The ID of the principal (user, group, or managed identity) to which the role will be assigned."
  type        = string
}
