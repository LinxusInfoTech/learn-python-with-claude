# Quick Start - Learn Python with Claude

Get started learning Python interactively in **2 minutes**.

## TL;DR - Just Run This

```bash
# 1. Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."

# 2. Run the app
learnwithclaude

# 3. Browser opens automatically → Start learning!
```

---

## Option 1: Local (Fastest)

### Install

```bash
cd /home/sachin/ai-mentor-lab
source .venv/bin/activate
pip install -e .
```

### Run

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
learnwithclaude
```

**Browser opens at:** http://localhost:8000

---

## Option 2: Docker (No Local Setup)

### Run

```bash
cd /home/sachin/ai-mentor-lab

export ANTHROPIC_API_KEY="sk-ant-..."
docker-compose up --build
```

**Browser opens at:** http://localhost:8000

---

## Option 3: Kubernetes (Production)

### Prerequisites
- Kubectl configured
- Kubernetes cluster running

### Deploy

```bash
# 1. Edit k8s/secrets.yaml with your API key
nano k8s/secrets.yaml

# 2. Apply manifests
kubectl apply -f k8s/

# 3. Port forward
kubectl port-forward svc/learn-python-with-claude 8000:80
```

**Browser opens at:** http://localhost:8000

---

## Commands

### Local

```bash
learnwithclaude              # Default (http://localhost:8000)
lwc                          # Short alias
learnwithclaude --port 9000  # Custom port
learnwithclaude --no-browser # Don't auto-open browser
```

### Docker

```bash
docker-compose up            # Start
docker-compose down          # Stop
docker-compose logs -f       # View logs
```

### Kubernetes

```bash
kubectl apply -f k8s/        # Deploy
kubectl delete -f k8s/       # Remove
kubectl logs -f deployment/learn-python-with-claude  # Logs
kubectl port-forward svc/learn-python-with-claude 8000:80  # Access
```

---

## API Key Setup

### Get your API key

1. Go to https://console.anthropic.com/keys
2. Create a new API key
3. Copy it

### Set it

**Option A: Environment Variable**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
learnwithclaude
```

**Option B: Save Permanently**
```bash
learnwithclaude
# When prompted, enter your API key and choose "save for future use"
# It's stored in: ~/.learn-python-with-claude/.env (encrypted permissions)
```

---

## How to Use

1. **Open the app** → Click a lesson on the left
2. **Read the content** → Study the concept and code examples
3. **Ask Claude** → Type your question in the chat panel
4. **Select & ask** → Highlight text/code and ask about it
5. **Practice** → Complete challenges

---

## Lessons

- **Variables** - Labeled boxes that hold values
- **Types** - Strings, integers, floats, booleans
- **F-Strings** - Combining variables into readable text
- **Functions** - Reusable code patterns

---

## Troubleshooting

### "API key required"
```bash
export ANTHROPIC_API_KEY="your-actual-key"
```

### Port already in use
```bash
learnwithclaude --port 9000
```

### Can't connect to browser
```bash
learnwithclaude --no-browser
# Then manually open: http://localhost:8000
```

### Docker build fails
```bash
# Clean and rebuild
docker-compose down
docker system prune
docker-compose up --build
```

---

## Next Steps

- Read [DEPLOYMENT.md](DEPLOYMENT.md) for advanced setup
- Check [README.md](README.md) for full documentation
- Ask Claude directly in the app for help!

---

**🚀 Happy Learning!**
