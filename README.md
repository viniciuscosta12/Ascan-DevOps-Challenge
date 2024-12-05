# Ascan-DevOps-Challenge

## Sumary

- [DevOps Ascan](#devops-ascan)
    - [About the project](#about-the-project)
    - [Technologies](#technologies)
    - [Getting Started](#getting-started)
        - [Prerequisites](#prerequisites)
        - [Create a cluster with terraform](#create-a-cluster-with-terraform)
        - [Connection with cluster](#connection-with-cluster)
- [Deploy App and Addons Using Terraform](#deploy-app-and-addons-using-terraform)
- [Usage](#usage)

# DevOps Ascan

This project is part of the conclusion of a DevOps training program at [Instituto Altântico](https://www.atlantico.com.br/).
The primary goal was to develop a straightforward website that could be deployed on Azure using Infrastructure as Code (IaC) tools like Terraform, containerized with Docker, and integrated with CI/CD workflows, while also including monitoring functionalities.

## About the project

The developed website is a simple "Hello World" application. The infrastructure was set up using AKS (Azure Kubernetes Service) and is monitored with the kube-prometheus-stack. The Kubernetes cluster runs a Helm chart that deploys a Docker image (inside a pod) sourced from DockerHub. This image contains the application built with Flask, a Python framework. The AKS cluster was provisioned using Terraform for Infrastructure as Code. Updates to the Docker image are automated through GitHub Actions workflows, which are triggered whenever changes are made to the application code. These workflows are initiated by pull requests and pushes to the main branch.

## Technologies

- Terraform (Infrastructure as Code)
- AKS (Azure Kubernetes Service)
- Helm (Create a chart)
- Docker (Containerization)
- Python (For the web application)
- GitHub Actions (Continuous Integration and Continuous Deployment)

## Getting Started

### Prerequisites
- Terraform installed on your local machine.
- An Azure account with necessary permissions to create resources.
- Azure CLI installed and configured with your Azure account.

### Create a cluster with terraform

Initialize Terraform in your project directory:
````sh
    terraform -chdir="iac/aks-cluster" init
````

Validate your configuration to ensure it’s correctly set up:
````sh
    terraform -chdir="iac/aks-cluster" validate
````

Preview the changes that Terraform plans to make to your infrastructure:
````sh
    terraform -chdir="iac/aks-cluster" plan
````

If everything is correct, apply the configuration to create the AKS cluster:
````sh
    terraform -chdir="iac/aks-cluster" apply
````

### Connection with cluster
Use the az aks get-credentials command to retrieve the AKS cluster credentials and set up the context in your local environment:
````sh
az aks get-credentials --resource-group <resource-group-name> --name <cluster-name>
````
>This creates or updates the ~/.kube/config file on your system, adding the cluster context.

#### Verify Cluster Access

To verify that your `kubeconfig` is correctly configured:
````sh
kubectl get nodes
````
>This command should display a list of the nodes in your AKS cluster, confirming that you have access.

## Deploy App and Addons Using Terraform
- Applications that need to be deployed to the AKS cluster can be managed using Terraform.

#### App
Install the application Hello World.
Initialize Terraform in your project directory:
````sh
    terraform -chdir="iac/addons/app" init
````

Preview the changes that Terraform plans to make to your infrastructure:
````sh
    terraform -chdir="iac/addons/app" plan
````

If everything is correct, apply the configuration to create the AKS cluster:
````sh
    terraform -chdir="iac/addons/app" apply
````
Use `-auto-approve` to apply automatically without a confirmation prompt.

To verify that your `install` is correctly:
````sh
kubectl get all -n app
````
#### Destruction
- To remove all managed resources:
````sh
   terraform -chdir="iac/addons/app" destroy
````

#### [Kube Prometheus Stack](https://github.com/prometheus-operator/kube-prometheus)

Installs the kube-prometheus-stack, a collection of Kubernetes manifests, [Grafana](http://grafana.com/) dashboards, [Prometheus rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) and  combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with [Prometheus](https://prometheus.io/) using the Prometheus Operator.

Initialize Terraform in your project directory:
````sh
    terraform -chdir="iac/addons/kube-prometheus-stack" init
````

Preview the changes that Terraform plans to make to your infrastructure:
````sh
    terraform -chdir="iac/addons/kube-prometheus-stack" plan
````

If everything is correct, apply the configuration to create the AKS cluster:
````sh
    terraform -chdir="iac/addons/kube-prometheus-stack" apply
````
Use `-auto-approve` to apply automatically without a confirmation prompt.

To verify that your `install` is correctly:
````sh
kubectl get all -n monitoring
````
#### Destruction
- To remove all managed resources:
````sh
   terraform -chdir="iac/addons/kube-prometheus-stack" destroy
````

## Usage
After deployment, the website can be accessed via the service's External IP. To retrieve the IP, run the following command:
````sh
   kubectl get svc -n app
````

To access the Grafana Dashboards can be accessed via the service's External IP. To retrieve the IP, run the following command and search for service prometheus-stack-grafana:
````sh
   kubectl get svc -n monitoring
````