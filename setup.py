"""
Setup script for AgenticOptio.

This setup script configures the AgenticOptio package for installation
using setuptools. It defines package metadata, dependencies, and
installation requirements for the AgenticOptio library.

Package Information:
    - Name: agenticoptio
    - Version: 0.1.0
    - Description: Minimal AI agent library focused on Ollama integration
    - Author: Raja CSP Raman
    - License: MIT

Dependencies:
    - openai>=1.0.0 (required for Ollama API compatibility)
    - pytest>=6.0 (development/testing)
    - pytest-asyncio>=0.21.0 (async testing support)

Python Support:
    - Python 3.8+ (modern async/await support required)
    - Cross-platform compatibility (Windows, macOS, Linux)

Installation:
    pip install -e .  # Development installation
    pip install agenticoptio  # Production installation
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agenticoptio",
    version="0.1.0",
    author="Raja CSP Raman",
    author_email="raja.csp@gmail.com",
    description="Minimal AI agent library focused on Ollama integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kactlabs/agenticoptio",
    project_urls={
        "Documentation": "https://agenticoptio.readthedocs.io/en/latest/",
        "Source": "https://github.com/kactlabs/agenticoptio",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.21.0",
        ],
    },
)