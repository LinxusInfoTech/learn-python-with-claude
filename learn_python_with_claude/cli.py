"""CLI for Learn Python with Claude"""
import os
import sys
import webbrowser
import time
import signal
import subprocess
from pathlib import Path
import click


def get_api_key():
    """Get or prompt for Anthropic API key"""
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if api_key:
        return api_key

    # Check if .env file exists in home directory
    env_file = Path.home() / ".learn-python-with-claude" / ".env"
    env_file.parent.mkdir(exist_ok=True)

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
                    if api_key:
                        os.environ["ANTHROPIC_API_KEY"] = api_key
                        return api_key

    # Prompt user
    click.echo("\n" + "="*60)
    click.echo("🔑 Anthropic API Key Required")
    click.echo("="*60)
    click.echo("\nYou need an Anthropic API key to use this tool.")
    click.echo("Get one at: https://console.anthropic.com/keys\n")

    api_key = click.prompt("Enter your API key", hide_input=True)

    if not api_key:
        click.echo("\n❌ API key is required. Exiting.")
        sys.exit(1)

    # Save for future use
    save_key = click.confirm("\nSave this key for future use?", default=True)
    if save_key:
        with open(env_file, "w") as f:
            f.write(f"ANTHROPIC_API_KEY={api_key}\n")
        os.chmod(env_file, 0o600)  # Restrict permissions
        click.echo(f"✅ Key saved to {env_file}")

    os.environ["ANTHROPIC_API_KEY"] = api_key
    return api_key


def open_browser(url, delay=2):
    """Open browser after a short delay"""
    def _open():
        time.sleep(delay)
        webbrowser.open(url)

    import threading
    thread = threading.Thread(target=_open, daemon=True)
    thread.start()


@click.command()
@click.option("--port", default=8000, help="Port to run server on (default: 8000)")
@click.option("--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)")
@click.option("--no-browser", is_flag=True, help="Don't auto-open browser")
def main(port, host, no_browser):
    """Learn Python interactively with Claude AI 🚀"""

    click.echo("\n" + "="*60)
    click.echo("🎓 Learn Python with Claude")
    click.echo("="*60 + "\n")

    # Check API key
    api_key = get_api_key()
    if not api_key:
        sys.exit(1)

    click.echo(f"✅ API key configured\n")

    # Start server
    url = f"http://{host}:{port}"
    click.echo(f"🚀 Starting server on {url}")
    click.echo(f"📚 Open your browser and start learning!\n")

    if not no_browser:
        open_browser(url)
        click.echo("⏳ Opening browser...\n")

    click.echo("Press Ctrl+C to stop\n" + "-"*60 + "\n")

    # Import here to avoid issues if dependencies not installed yet
    import uvicorn
    from .server import app

    try:
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level="warning"
        )
    except KeyboardInterrupt:
        click.echo("\n\n👋 Thanks for learning! See you next time.")
        sys.exit(0)


if __name__ == "__main__":
    main()
