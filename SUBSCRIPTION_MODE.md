# Subscription Mode - Learn Python with Claude

Run the interactive learning app using **your Claude subscription** instead of API keys.

## ✨ What is Subscription Mode?

- ✅ **No API key needed**
- ✅ **Uses your Claude subscription**
- ✅ **Questions prepared locally**
- ✅ **Sent to Claude.ai when you're ready**

## 🚀 Quick Start

### 1. Install

```bash
cd learn-python-with-claude
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### 2. Run (Subscription Mode)

```bash
lwc-sub
# or
learnwithclaude-sub
```

### 3. Browser Opens

Opens at http://localhost:8000

---

## 📖 How to Use

### Step 1: Select a Lesson
Click on any lesson in the left panel (Variables, Types, F-Strings, Functions)

### Step 2: Read Content
Study the concept and code examples

### Step 3: Ask a Question
Type your question in the chat panel on the right:
- "What does `def` mean?"
- "Explain this code line by line"
- "Give me a practice exercise"

### Step 4: Send to Claude
Two options:

**Option A: Open Claude.ai**
```
Click "Open Claude.ai ↗"
→ Claude.ai opens in new tab
→ Your question is copied to clipboard
→ Paste it and ask
→ Get instant answer from Claude
```

**Option B: Copy Question**
```
Click "Copy Question"
→ Your prepared message is copied
→ Go to claude.ai manually
→ Paste and ask
```

---

## 💡 Example Workflow

```
1. Open Learn Python app (lwc-sub)
2. Click "Variables" lesson
3. Read about variables
4. Select the code: name = "Sachin"
5. Type in chat: "What does the = sign do?"
6. Click "Open Claude.ai"
7. Claude.ai opens with your question ready
8. Paste and get instant explanation
9. Come back to app and continue learning
```

---

## 🔄 Mode Comparison

### API Key Mode (lwc)
```
Your Computer
    ↓
Learn Python App
    ↓
Claude API (costs money)
    ↓
Response back to app
```

### Subscription Mode (lwc-sub)
```
Your Computer
    ↓
Learn Python App
    ↓
[Prepares context locally]
    ↓
Claude.ai (your subscription)
    ↓
Response in browser
```

---

## 🎯 Features

| Feature | Subscription | API Key |
|---------|--------------|---------|
| Cost | Free (your subscription) | Per API call |
| Setup | No API key | Need API key |
| Speed | Instant prep, then Claude.ai | Direct response |
| Privacy | Claude.ai handles data | Direct API call |
| Multi-browser | Yes (claude.ai) | Single app |

---

## 📝 Commands

```bash
# Subscription mode (default port 8000)
lwc-sub

# Custom port
lwc-sub --port 9000

# Don't auto-open browser
lwc-sub --no-browser

# Full name
learnwithclaude-sub

# Show help
lwc-sub --help
```

---

## 🐳 Docker Subscription Mode

Create a `docker-compose.sub.yml`:

```yaml
version: '3.8'

services:
  learn-python:
    build: .
    container_name: learn-python-subscription
    ports:
      - "8000:8000"
    volumes:
      - ./01-python-basics:/app/01-python-basics
    restart: unless-stopped
    command: ["learnwithclaude-sub", "--host", "0.0.0.0"]
```

Run with:
```bash
docker-compose -f docker-compose.sub.yml up --build
```

---

## ⚙️ How It Works

1. **Lessons stored locally** in the app
2. **Your question** + lesson context prepared
3. **Ready to send** to Claude.ai
4. **You paste** in Claude.ai
5. **Get response** using your subscription
6. **No API costs**

---

## 🛡️ Privacy

- Your questions are prepared **locally** on your computer
- Sent to **Claude.ai only when you click "Open"**
- Not stored on any server
- Full control over what gets sent

---

## ❓ FAQ

**Q: Do I need an API key?**
A: No! Subscription mode uses Claude.ai (your subscription).

**Q: Is it slower than API key mode?**
A: Slightly (you manually go to Claude.ai), but no costs.

**Q: Can I use both modes?**
A: Yes! Use `lwc` for API mode, `lwc-sub` for subscription mode.

**Q: What if I don't have a Claude subscription?**
A: Get one at https://claude.ai/pricing or use API key mode (lwc).

**Q: Can I run this offline?**
A: The lessons load offline, but you need internet to use Claude.ai.

---

## 🚀 Next Steps

1. **Install**: `pip install -e .`
2. **Run**: `lwc-sub`
3. **Learn**: Select a lesson
4. **Ask Claude**: Type questions, get answers
5. **Practice**: Complete challenges
6. **Progress**: Check ROADMAP.md for what's next

---

## 💬 Support

Having issues? 

```bash
# Check if installed
lwc-sub --help

# Reinstall
pip install -e . --force-reinstall

# Use help
lwc-sub --help
```

---

**Happy Learning! 🎓**

No API keys. No costs. Just you, Claude, and Python. 🚀
