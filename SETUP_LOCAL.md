# Setup & Run Locally - Learn Python with Claude

Complete step-by-step guide to run the interactive learning app on your computer using your Claude subscription.

---

## **🚀 5-Minute Setup**

### **Prerequisite: Clone the repo**

```bash
cd ~
git clone git@github.com:LinxusInfoTech/learn-python-with-claude.git
cd learn-python-with-claude
```

---

## **✅ Method 1: Subscription Mode (Recommended - No API Key)**

Best for learning with your existing Claude subscription.

### **Step 1: Create Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal.

### **Step 2: Install Package**

```bash
pip install -e .
```

This installs all dependencies (FastAPI, Anthropic SDK, Click, etc.)

### **Step 3: Run the App**

```bash
lwc-sub
```

**That's it!** Browser opens automatically at http://localhost:8000

### **Step 4: Start Learning**

1. **Select a lesson** from left panel
2. **Read the content**
3. **Type a question** in the chat panel
4. **Click "Open Claude.ai ↗"**
5. **Your question is ready** in Claude.ai
6. **Paste and learn!**

---

## **💳 Method 2: API Key Mode (Advanced)**

If you want direct responses in the app (costs money per API call).

### **Step 1-2: Same as above**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### **Step 3: Get API Key**

1. Go to https://console.anthropic.com/keys
2. Create a new API key
3. Copy it

### **Step 4: Set Environment Variable**

```bash
export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY_HERE"
```

Replace `YOUR_KEY_HERE` with your actual key.

### **Step 5: Run the App**

```bash
learnwithclaude
# or short form
lwc
```

Browser opens at http://localhost:8000

### **Step 6: Start Learning**

1. **Select a lesson**
2. **Type a question**
3. **Get instant response** from Claude (costs money)

---

## **🐳 Method 3: Docker (No Local Setup)**

If you don't want to install Python locally.

### **Prerequisites**

- Docker installed
- Docker Compose installed

### **Step 1: Clone repo**

```bash
cd ~
git clone git@github.com:LinxusInfoTech/learn-python-with-claude.git
cd learn-python-with-claude
```

### **Step 2: Subscription Mode**

```bash
# Just run it - no environment setup needed
docker-compose up --build
```

Browser opens at http://localhost:8000

### **Step 3: API Key Mode**

```bash
# Set your API key
export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY_HERE"

# Run with Docker
docker-compose up --build
```

---

## **⌨️ All Commands**

### **Subscription Mode (No costs, uses your subscription)**

```bash
lwc-sub                          # Default (localhost:8000)
learnwithclaude-sub             # Full name
lwc-sub --port 9000             # Custom port
lwc-sub --no-browser            # Don't auto-open browser
lwc-sub --help                  # Show help
```

### **API Key Mode (Direct responses, costs money)**

```bash
learnwithclaude                  # Default
lwc                              # Short form
learnwithclaude --port 9000     # Custom port
lwc --no-browser                # Don't auto-open browser
learnwithclaude --help          # Show help
```

### **Docker**

```bash
docker-compose up --build        # Start
docker-compose down              # Stop
docker-compose logs -f           # View logs
docker-compose ps                # Check status
```

---

## **🐛 Troubleshooting**

### **"Command not found: lwc-sub"**

**Solution:** Make sure venv is activated:
```bash
source venv/bin/activate
```

Then try again:
```bash
lwc-sub
```

### **"ModuleNotFoundError"**

**Solution:** Reinstall package:
```bash
source venv/bin/activate
pip install -e . --force-reinstall
```

### **"Port 8000 already in use"**

**Solution:** Use different port:
```bash
lwc-sub --port 9000
```

### **"Python not found"**

**Solution:** Make sure Python 3.8+ is installed:
```bash
python3 --version
```

On macOS:
```bash
brew install python3
```

On Ubuntu/Debian:
```bash
sudo apt-get install python3
```

### **"API key required" (API Key Mode)**

**Solution:** Set your API key:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
learnwithclaude
```

### **Browser doesn't open automatically**

**Solution:** Open manually and use flag:
```bash
lwc-sub --no-browser
# Then manually open: http://localhost:8000
```

### **Docker build fails**

**Solution:** Clean and rebuild:
```bash
docker-compose down
docker system prune -a
docker-compose up --build
```

---

## **📊 Comparison**

| Feature | Subscription Mode | API Key Mode | Docker |
|---------|------------------|--------------|--------|
| **Cost** | Free (your subscription) | Pay per use | Free |
| **Setup** | 2 minutes | 3 minutes | 2 minutes |
| **Speed** | Prepare + Claude.ai | Direct (fast) | Same as local |
| **API Key** | ❌ Not needed | ✅ Required | ✅ Required (or subscription mode) |
| **Internet** | ✅ Needed for Claude | ✅ Needed | ✅ Needed |
| **Privacy** | ✅ Good (local prep) | ⚠️ API call logs | ✅ Good |

---

## **🎯 Next Steps**

Once running, you'll see:

1. **Left Panel** → Select lessons
2. **Middle** → Read content
3. **Right Panel** → Ask questions
4. **Browser** → Opens claude.ai (subscription mode) or shows responses (API key mode)

---

## **📝 Workflow Example**

```
1. Open terminal
2. cd learn-python-with-claude
3. source venv/bin/activate
4. lwc-sub
5. Browser opens → Click "Variables" lesson
6. Read about variables
7. Type: "What is the = sign?"
8. Click "Open Claude.ai ↗"
9. Claude.ai opens + question copied
10. Paste + get instant explanation
11. Back to app, continue learning!
```

---

## **⚡ Quick Copy-Paste Setup**

**Subscription Mode (Recommended):**
```bash
cd ~
git clone git@github.com:LinxusInfoTech/learn-python-with-claude.git
cd learn-python-with-claude
python3 -m venv venv
source venv/bin/activate
pip install -e .
lwc-sub
```

**API Key Mode:**
```bash
cd ~
git clone git@github.com:LinxusInfoTech/learn-python-with-claude.git
cd learn-python-with-claude
python3 -m venv venv
source venv/bin/activate
pip install -e .
export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY_HERE"
learnwithclaude
```

**Docker (Subscription):**
```bash
cd ~
git clone git@github.com:LinxusInfoTech/learn-python-with-claude.git
cd learn-python-with-claude
docker-compose up --build
```

---

## **🔗 Resources**

- **GitHub**: https://github.com/LinxusInfoTech/learn-python-with-claude
- **Subscription Mode Docs**: SUBSCRIPTION_MODE.md
- **Full Docs**: README.md
- **Deployment**: DEPLOYMENT.md
- **Roadmap**: ROADMAP.md

---

**You're all set! 🎓 Happy learning!**

Questions? Check SUBSCRIPTION_MODE.md or README.md for more details.
