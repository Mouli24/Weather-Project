# 🌦️ Weather Alert CLI Tool  
A powerful, multi-feature command-line weather monitoring system built in Python.  
This tool fetches real-time weather, displays it beautifully in the terminal, shows GUI maps, sends desktop notifications, handles alerts, exports data, and caches city weather intelligently.

------------------------------------------------
Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

------------------------------------------------
## 🚀 Features

### ✅ **1. Multi-City Weather Fetching (Threaded)**
Fetch weather data for multiple cities simultaneously using `ThreadPoolExecutor` for ultra-fast performance.