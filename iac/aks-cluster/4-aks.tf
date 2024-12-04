resource "azurerm_kubernetes_cluster" "this" {
  name                = "${local.env}-${local.aks_name}"
  location            = var.default_location
  resource_group_name = var.resgroup_name
  dns_prefix          = "ascanaks1"

  kubernetes_version        = "1.29.9"
  automatic_upgrade_channel = "stable"
  private_cluster_enabled   = false
  node_resource_group       = "${local.resource_group_name}-${local.env}-${local.aks_name}"

  sku_tier = "Free"

  oidc_issuer_enabled       = true
  workload_identity_enabled = true

  network_profile {
    network_plugin = "azure"
    dns_service_ip = "10.0.64.10"
    service_cidr   = "10.0.64.0/19"
  }

  default_node_pool {
    name                 = "general"
    temporary_name_for_rotation = "rotation"
    vm_size              = local.vm_size
    vnet_subnet_id       = azurerm_subnet.subnet1.id
    type                 = "VirtualMachineScaleSets"
    node_count           = local.node_count
    orchestrator_version = local.orchestrator_version

    node_labels = {
      role = "general"
    }
  }

  identity {
    type         = "SystemAssigned"
  }

  tags = {
    Projeto = local.projeto
    Environment  = local.env
  }

  lifecycle {
    ignore_changes = [default_node_pool[0].node_count]
  }
  
  }
