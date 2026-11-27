from setuptools import setup, find_packages

setup(
    name="api-badger",
    version="1.0.0",
    description="Generate badges for public APIs from README.md",
    author="API Badger",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "markdown>=3.4.0",
        "jinja2>=3.0.0",
        "flask>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "api-badger=api_badger.cli:main",
        ]
    },
    python_requires=">=3.8",
)