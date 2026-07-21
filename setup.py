"""Setup script for learn-python-with-claude package"""
from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text()

setup(
    name="learn-python-with-claude",
    version="0.1.0",
    description="Interactive Python learning with Claude AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sachin",
    author_email="sachinj7008@gmail.com",
    url="https://github.com/yourusername/learn-python-with-claude",
    license="MIT",
    packages=find_packages(),
    package_data={
        "learn_python_with_claude": ["assets/*.html"],
    },
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "anthropic>=0.21.0",
        "click>=8.1.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "learnwithclaude=learn_python_with_claude.cli:main",
            "lwc=learn_python_with_claude.cli:main",
            "lwc-sub=learn_python_with_claude.cli_subscription:main",
            "learnwithclaude-sub=learn_python_with_claude.cli_subscription:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="python learning claude ai education interactive",
)
