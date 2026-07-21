# Deployment Guide - Learn Python with Claude

Complete guide to deploy the application locally, with Docker, and on Kubernetes.

## Table of Contents

1. [Local Installation](#local-installation)
2. [Docker Deployment](#docker-deployment)
3. [Kubernetes Deployment](#kubernetes-deployment)
4. [GitHub Actions CI/CD](#github-actions-cicd)

---

## Local Installation

### Prerequisites
- Python 3.8+
- pip
- Anthropic API key

### Steps

1. **Clone and setup**
   ```bash
   cd /home/sachin/ai-mentor-lab
   source .venv/bin/activate
   pip install -e .
   ```

2. **Set your API key**
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```

3. **Run the app**
   ```bash
   learnwithclaude
   # or
   lwc
   ```

4. **Open browser** → http://localhost:8000

---

## Docker Deployment

### Quick Start with Docker Compose

```bash
cd /home/sachin/ai-mentor-lab

# Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Start the app
docker-compose up --build
```

Then open: http://localhost:8000

### Manual Docker Build

```bash
# Build the image
docker build -t learn-python-with-claude:latest .

# Run the container
docker run -p 8000:8000 \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  learn-python-with-claude:latest
```

### Docker Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | Yes | - | Your Anthropic API key |
| `PORT` | No | 8000 | Port to run on |
| `HOST` | No | 0.0.0.0 | Host to bind to |

### Docker Network

To expose on different host:
```bash
docker run -p 0.0.0.0:8000:8000 \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  learn-python-with-claude:latest
```

---

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (1.24+)
- kubectl configured
- Docker image in registry (ghcr.io or Docker Hub)
- Ingress controller (nginx recommended)

### Step 1: Create Namespace (optional)

```bash
kubectl create namespace learn-python
```

### Step 2: Create Secrets

Edit `k8s/secrets.yaml` and replace `YOUR_API_KEY` with your actual key:

```bash
# Option A: Edit and apply manually
kubectl apply -f k8s/secrets.yaml

# Option B: Create from command line
kubectl create secret generic learn-python-secrets \
  --from-literal=anthropic-api-key="sk-ant-..." \
  -n default
```

### Step 3: Deploy

```bash
# Apply all manifests
kubectl apply -f k8s/

# Or individually
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/ingress.yaml
```

### Step 4: Verify Deployment

```bash
# Check pods
kubectl get pods -l app=learn-python-with-claude

# Check service
kubectl get svc learn-python-with-claude

# Check ingress
kubectl get ingress learn-python-ingress

# View logs
kubectl logs -f deployment/learn-python-with-claude
```

### Step 5: Access the App

```bash
# Port forward to localhost
kubectl port-forward svc/learn-python-with-claude 8000:80

# Then open: http://localhost:8000
```

Or if you have an ingress configured:
```
https://learn-python.example.com
```

### Scaling

```bash
# Scale to 3 replicas
kubectl scale deployment learn-python-with-claude --replicas=3

# Check status
kubectl get deployment learn-python-with-claude
```

### Updating Deployment

```bash
# Update image
kubectl set image deployment/learn-python-with-claude \
  app=ghcr.io/yourusername/learn-python-with-claude:v1.0.0

# Check rollout status
kubectl rollout status deployment/learn-python-with-claude

# Rollback if needed
kubectl rollout undo deployment/learn-python-with-claude
```

### Monitoring

```bash
# Get resource usage
kubectl top pods -l app=learn-python-with-claude

# Describe deployment
kubectl describe deployment learn-python-with-claude

# View recent events
kubectl get events --sort-by='.lastTimestamp'
```

---

## GitHub Actions CI/CD

### Setup

1. **Enable GitHub Actions** in your repository

2. **Add Secrets** to your repository settings:
   - `DOCKER_USERNAME` - Docker Hub username (or leave empty for ghcr.io)
   - `DOCKER_PASSWORD` - Docker Hub token (or leave empty for ghcr.io)
   - `KUBE_CONFIG` - Base64 encoded kubeconfig file
   - `SLACK_WEBHOOK_URL` - Optional: Slack webhook for notifications

3. **Get kubeconfig (if deploying to K8s)**
   ```bash
   # Encode your kubeconfig
   cat ~/.kube/config | base64 -w 0
   
   # Copy the output and add as KUBE_CONFIG secret
   ```

### Workflows

#### 1. Build Workflow (`.github/workflows/build.yml`)

Triggers on:
- Push to `main` branch
- Push of tags (v*)
- Pull requests

Actions:
- Builds Docker image
- Pushes to registry (if not PR)
- Caches layers for speed

#### 2. Test Workflow (`.github/workflows/test.yml`)

Triggers on:
- Push to `main` and `develop`
- Pull requests

Tests:
- Python 3.8, 3.9, 3.10, 3.11, 3.12
- Code formatting (Black)
- Linting (flake8)
- Type checking (mypy)
- Unit tests with coverage
- Uploads coverage to Codecov

#### 3. Deploy Workflow (`.github/workflows/deploy.yml`)

Triggers on:
- Push to `main` branch (latest tag)
- Push of version tags
- Manual trigger (`workflow_dispatch`)

Actions:
- Updates Kubernetes deployment
- Waits for rollout
- Sends Slack notification

### Local Workflow Testing

Test workflows locally with `act`:

```bash
# Install act
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

# Run specific workflow
act -j build

# Run all workflows
act

# With secrets
act -s ANTHROPIC_API_KEY="sk-ant-..."
```

---

## Troubleshooting

### Docker Issues

```bash
# Check image was built
docker images | grep learn-python

# View logs
docker logs <container-id>

# Shell into container
docker exec -it <container-id> sh
```

### Kubernetes Issues

```bash
# Check pod status
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Test connectivity
kubectl exec -it <pod-name> -- curl http://localhost:8000/api/lessons

# Port forward for debugging
kubectl port-forward pod/<pod-name> 8000:8000
```

### API Key Not Working

```bash
# Verify secret exists
kubectl get secret learn-python-secrets -o yaml

# Check if mounted correctly
kubectl exec -it <pod-name> -- env | grep ANTHROPIC_API_KEY

# Update secret
kubectl delete secret learn-python-secrets
kubectl create secret generic learn-python-secrets \
  --from-literal=anthropic-api-key="new-key"
```

---

## Performance Tuning

### Resource Limits (Kubernetes)

Edit `k8s/deployment.yaml`:
```yaml
resources:
  requests:
    cpu: 100m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

### Replicas

Edit `k8s/deployment.yaml`:
```yaml
spec:
  replicas: 3  # Increase for higher traffic
```

### Docker Memory

```bash
docker run -m 512m learn-python-with-claude:latest
```

---

## Production Checklist

- [ ] API key securely stored (not in code)
- [ ] Health checks configured
- [ ] Resource limits set
- [ ] Ingress configured with TLS
- [ ] Monitoring/logging setup
- [ ] Backups configured
- [ ] Scaling policy defined
- [ ] Rate limiting enabled
- [ ] Security context applied (non-root user)
- [ ] Network policies configured

---

## Support

For issues:
1. Check logs: `kubectl logs -f deployment/learn-python-with-claude`
2. Check events: `kubectl get events --sort-by='.lastTimestamp'`
3. File an issue with logs attached

Happy learning! 🚀
