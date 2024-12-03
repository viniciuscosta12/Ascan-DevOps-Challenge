## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 3.75.0 |
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | >= 2.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 3.75.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [azurerm_kubernetes_cluster.this](https://registry.terraform.io/providers/hashicorp/azurerm/3.75.0/docs/resources/kubernetes_cluster) | resource |
| [azurerm_subnet.subnet1](https://registry.terraform.io/providers/hashicorp/azurerm/3.75.0/docs/resources/subnet) | resource |
| [azurerm_subnet.subnet2](https://registry.terraform.io/providers/hashicorp/azurerm/3.75.0/docs/resources/subnet) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_default_location"></a> [default\_location](#input\_default\_location) | n/a | `string` | `"eastus2"` | no |
| <a name="input_resgroup_name"></a> [resgroup\_name](#input\_resgroup\_name) | n/a | `string` | `"autopilot-ia-dev"` | no |
| <a name="input_storage_account"></a> [storage\_account](#input\_storage\_account) | n/a | `string` | `"autopilotstoragetf"` | no |

## Outputs

No outputs.
