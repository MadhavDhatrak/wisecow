# Wisecow Application

## 📋 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [TLS Setup](#tls-setup)
- [Screenshots](#screenshots)
- [CI/CD Pipeline](#cicd-pipeline)
- [ArgoCD Setup](#argocd-setup)
- [Project Structure](#project-structure)
- [Verify Deployment](#verify-deployment)

## About

Wisecow displays random fortune messages with ASCII cow art. This project demonstrates:
- Docker containerization
- Kubernetes deployment
- TLS/HTTPS implementation
- GitHub Actions CI/CD
- ArgoCD GitOps

## Prerequisites

- Kubernetes cluster (Minikube)
- kubectl
- Docker
- Nginx Ingress Controller

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/MadhavDhatrak/wisecow.git
cd wisecow
```

### 2. Deploy to Kubernetes
```bash
# Deploy application
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

### 3. Setup Minikube Tunnel
```bash
# Run in separate terminal
minikube tunnel
```

### 4. Update Hosts File
Add to `/etc/hosts` or `C:\Windows\System32\drivers\etc\hosts`:
```
127.0.0.1  wisecow.local
```

### 5. Access Application
Open browser: **https://wisecow.local**

## TLS Setup

### Create TLS Certificate
```bash
# Generate certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout wisecow.key -out wisecow.crt \
  -subj "/CN=wisecow.local/O=wisecow"

# Create Kubernetes secret
kubectl create secret tls wisecow-tls \
  --cert=wisecow.crt \
  --key=wisecow.key
```

## Screenshots

### Browser with TLS
<img width="598" height="282" alt="image" src="https://github.com/user-attachments/assets/cb8bc7bb-474c-4ae4-a1f3-c31455fe4151" />


### ArgoCD Dashboard
<img width="1301" height="497" alt="Screenshot 2025-11-07 104803" src="https://github.com/user-attachments/assets/b1d84d9f-4376-4137-ad4d-1a96712dccee" />

## CI/CD Pipeline

GitHub Actions automatically:
- Builds Docker image on push
- Pushes to Docker Hub
- Updates Kubernetes manifests

**Required Secrets:**
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

## ArgoCD Setup

```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Deploy application
kubectl apply -f argocd/application.yaml

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## Project Structure

```
wisecow/
├── Dockerfile
├── wisecow.sh
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── argocd/
│   └── application.yaml
└── .github/workflows/
    └── ci-cd.yaml
```

## Verify Deployment

```bash
# Check pods
kubectl get pods

# Check service
kubectl get svc

# Check ingress
kubectl get ingress

# Test HTTPS
curl -k https://wisecow.local
```


