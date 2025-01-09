# Default location for all resources
variable "location" {
  default = "swedencentral"
}

# Base name for resources
variable "base_name" {
  default = "aifoundrysandbox" # Change this to your project or organization name
}

# Whether to allow hyphens in resource names
variable "allow_hyphens" {
  default = true
}

variable "subscription_id" {
  description = "The Azure subscription ID to use for this deployment."
  type        = string
}

variable "model_name" {
  description = "Name of the model"
  type        = string
  default     = "meta-llama3-8b"
}

variable "model_id" {
  description = "ID of the model"
  type        = string
  default     = "azureml://registries/azureml-meta/models/Meta-Llama-3-8B-Instruct"
}

