variable "resgroup_name" {
  type    = string
  default = "ASCAN" 
}

variable "default_location" {
  type    = string
  default = "westus2" 
}

variable "subscription_id" {
  description = "The Azure Subscription ID"
  type        = string
}
