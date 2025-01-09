# Write the YAML file to disk using the templatefile function
resource "local_file" "subscription_yml" {
  content  = templatefile("${path.module}/subscription.yml.tmpl", {
    name        = var.name
    model_id    = var.model_id
  })
  filename = "${path.module}/subscription.yml" # Adjust path as needed
}

# Use the YAML file in the local-exec provisioner
resource "null_resource" "model_subscription" {
  provisioner "local-exec" {
    command = <<EOT
        az ml marketplace-subscription create -f ${local_file.subscription_yml.filename} -g ${var.resource_group_name} -w ${var.workspace_name}
    EOT
  }

  # Ensure the YAML file is created before running the command
  depends_on = [local_file.subscription_yml]
}
