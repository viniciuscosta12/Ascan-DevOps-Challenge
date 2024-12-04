locals {
  env                  = "ASCAN"
  region               = "westus2"
  resource_group_name  = "ASCAN"
  aks_name             = "aks-ascan"
  eks_version          = "1.29.9"
  projeto              = "ASCAN"
  orchestrator_version = "1.29.9"
  node_count           = 2
  vm_size              = "Standard_B2ms"
}
