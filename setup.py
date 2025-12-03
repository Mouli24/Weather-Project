from setuptools import setup, find_packages

setup(
    name="weather-alert", 
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "weather-alert=weather_alert.main:main",
        ]
    },
    include_package_data=True,
    description="A CLI tool to fetch weather alerts using Open-Meteo API.",
    author="Aastha Priya",
    license="MIT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aasthap25/weather-alert",
)
