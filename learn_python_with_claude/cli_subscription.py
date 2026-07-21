"""CLI for Learn Python with Claude - Subscription Mode"""
import os
import sys
import webbrowser
import time
import signal
import subprocess
from pathlib import Path
import click


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
    """Learn Python interactively with Claude using your subscription 🚀

    No API key needed! Uses your Claude subscription through claude.ai
    """

    click.echo("\n" + "="*60)
    click.echo("🎓 Learn Python with Claude (Subscription Mode)")
    click.echo("="*60 + "\n")

    click.echo("✅ Subscription Mode Active")
    click.echo("   • No API key required")
    click.echo("   • Uses your Claude.ai subscription")
    click.echo("   • Questions prepared locally\n")

    # Start server
    url = f"http://{host}:{port}"
    click.echo(f"🚀 Starting server on {url}")
    click.echo(f"📚 Open your browser and start learning!\n")

    if not no_browser:
        open_browser(url)
        click.echo("⏳ Opening browser...\n")

    click.echo("How it works:")
    click.echo("1. Select a lesson and read the content")
    click.echo("2. Type your question in the chat panel")
    click.echo("3. Click 'Open Claude.ai' or 'Copy Question'")
    click.echo("4. Your question is prepared and ready to paste in Claude\n")

    click.echo("Press Ctrl+C to stop\n" + "-"*60 + "\n")

    # Import here to avoid issues if dependencies not installed yet
    import uvicorn
    from .server_no_api import app

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
