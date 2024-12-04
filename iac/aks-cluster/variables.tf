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
  default     = "b30f942d-212a-4a7f-8421-437f06604c7a"
}
