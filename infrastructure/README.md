# O.N.I.O.N Infrastructure

This directory contains Infrastructure as Code (IaC) for O.N.I.O.N.

## Structure

- `terraform/` - Terraform modules and environments
- `k8s/` - Kubernetes/Azure Container Apps manifests
- `scripts/` - Deployment and management scripts

## Environments

- **dev**: Development environment
- **staging**: Pre-production testing
- **prod**: Production environment

## Terraform

### Modules

Reusable Terraform modules for:
- Azure Container Apps
- Azure Key Vault
- Application Insights
- Networking (VNet, NSG)
- Database
- Storage

### Usage

```bash
cd terraform/environments/dev
terraform init
terraform plan
terraform apply
```

## Kubernetes

### Manifests

- Service deployments
- ConfigMaps
- Secrets (referenced from Key Vault)
- Ingress rules
- Network policies

### Usage

```bash
kubectl apply -f k8s/api-gateway.yaml
kubectl apply -f k8s/policy-pdp.yaml
```

## Deployment Scripts

- `deploy.sh`: Deploy to environment
- `rollback.sh`: Rollback deployment
- `health-check.sh`: Verify deployment health

## Security

- All secrets in Azure Key Vault
- No hardcoded credentials
- Network segmentation
- TLS everywhere
