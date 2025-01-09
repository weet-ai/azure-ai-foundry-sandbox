# Define the variables for the YAML content
variable "name" {
  description = "Name of the model"
  type        = string
}

variable "model_id" {
  description = "ID of the model"
  type        = string
}

variable "workspace_name" {
  description = "The name of the Azure Machine Learning workspace."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group containing the Azure Machine Learning workspace."
  type        = string
}