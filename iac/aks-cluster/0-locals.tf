locals {
  env                  = "ASCAN"
  region               = "eastus2"
  resource_group_name  = "ASCAN"
  eks_name             = "aks-ascan"
  eks_version          = "1.29.9"
  projeto              = "ASCAN"
  orchestrator_version = "1.29.9"
  node_count           = 2
  vm_size              = "Standard_B1s"
}
