resource "azurerm_virtual_network" "this" {
  name                = "main"
  address_space       = ["10.0.0.0/16"]
  location            = var.default_location
  resource_group_name = var.resgroup_name

  tags = {
    Projeto = local.projeto
    Environment  = local.env
  }
}
