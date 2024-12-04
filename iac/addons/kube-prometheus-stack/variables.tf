variable "resgroup_name" {
  type    = string
  default = "ASCAN" 
}

variable "aks_cluster_name" {
  type    = string
  default = "ASCAN-aks-ascan" 
}

variable "path_state" {
   type = string 
   default= "kube-prometheus-stack"
}