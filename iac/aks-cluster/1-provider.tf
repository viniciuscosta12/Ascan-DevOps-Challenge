provider "azurerm" {
  features {}
  skip_provider_registration = true
  subscription_id = var.subscription_id
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.8.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = ">= 2.1.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = var.resgroup_name
    storage_account_name = "autopilotstoragetf"
    container_name       = "terraformstate"
    key                  = "terraform/autopilot/state"
  }
}
