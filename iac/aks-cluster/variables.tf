variable "resgroup_name" {
  type    = string
  default = "ASCAN" 
}

variable "storage_account" {
  type    = string
  default = "autopilotstoragetf" 
}

variable "default_location" {
  type    = string
  default = "eastus2" 
}

variable "subscription_id" {
  description = "The Azure Subscription ID"
  type        = string
  default     = "fdf75646-7704-44d4-b49c-4562d51503c7"
}
