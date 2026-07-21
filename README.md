# Learn Python with Claude 🎓

An interactive Python learning platform where Claude AI teaches you programming concepts through hands-on examples.

## Features

- 📚 **Interactive Lessons** - Learn variables, types, f-strings, and functions
- 💬 **Ask Claude** - Ask questions about any lesson directly in the browser
- 🎯 **Select & Ask** - Highlight any code or text and ask Claude to explain it
- 🚀 **Fast Setup** - Single command to start learning
- 🔄 **Real-time** - Get instant explanations powered by Claude AI

## Installation

### Option 1: Install from this project (development mode)

```bash
cd /home/sachin/ai-mentor-lab
pip install -e .
```

### Option 2: Install from PyPI (when published)

```bash
pip install learn-python-with-claude
```

## Quick Start

1. **Set your Anthropic API key** (you'll be prompted on first run):
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```
   Or save it securely (the app will prompt you to save it)

2. **Start learning:**
   ```bash
   lpwc
   ```

3. **Browser opens automatically** → Start with any lesson from the left panel

4. **Ask Claude questions** → Type in the right panel, select text to ask about it

## Commands

```bash
# Start the learning session (default port 8000)
lpwc

# Custom port
lpwc --port 9000

# Don't auto-open browser
lpwc --no-browser

# Run with Python module
python -m learn_python_with_claude
```

## How to Use

1. **Select a Lesson** - Click on any lesson in the left sidebar
2. **Read Content** - Study the concept with code examples
3. **Ask Questions** - Type in the chat panel on the right
4. **Select & Ask** - Highlight any text/code and ask Claude about it
5. **Practice** - Complete challenges suggested by Claude

## Lessons Included

- **Variables** - Understanding labeled boxes that hold values
- **Types** - Strings, integers, floats, and booleans
- **F-Strings** - Combining variables into readable text
- **Functions** - Writing reusable code once and using it many times

## System Requirements

- Python 3.8+
- Modern web browser
- Anthropic API key (free trial available)

## Troubleshooting

### "API key is required"
```bash
# Set your API key before running
export ANTHROPIC_API_KEY="your-key-here"
lpwc
```

### Port already in use
```bash
# Use a different port
lpwc --port 9000
```

### Browser doesn't open
```bash
# Run without auto-open, then visit manually
lpwc --no-browser
# Then open: http://localhost:8000
```

## API Key Management

Your API key is stored in `~/.learn-python-with-claude/.env` (with restricted permissions).

To use a different key:
```bash
export ANTHROPIC_API_KEY="new-key-here"
lpwc
```

## Development

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Build package
python setup.py sdist bdist_wheel
```

## License

MIT

## Credits

Built by Sachin for learning Python interactively with Claude AI.

---

**Happy Learning! 🚀**

Need help? Ask Claude directly in the app - just type your question in the chat panel.
