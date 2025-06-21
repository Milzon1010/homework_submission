import requests
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.parse
import csv

# =============================================================================
# STEP 1: BASIC HTTP REQUESTS - MEMAHAMI DASAR-DASAR HTTP
# =============================================================================
# 1️⃣ Simple GET request - Ambil daftar provinsi
print("\n#1: Simple GET Request - Get Indonesian Provinces")

try:
    response = requests.get("https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json")
    response.raise_for_status()
    provinces = response.json()
    
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Total Provinces: {len(provinces)}")
    print("📌 First 3 Provinces:")
    for p in provinces[:3]:
        print(f"- {p['name']}")

except Exception as e:
    print(f"❌ Error fetching provinces: {e}")

# 2️⃣ GET request with headers
print("\n#2: Request with Custom Headers")

headers = {
    "User-Agent": "Mozilla/5.0 (LatihanAPI/1.0)",
    "Accept": "application/json"
}

try:
    response = requests.get("https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json", headers=headers)
    response.raise_for_status()
    print(f"✅ Headers sent successfully: {response.status_code}")
    print(f"✅ Sample Province: {response.json()[0]['name']}")
except Exception as e:
    print(f"❌ Error with headers: {e}")

# 3️⃣ Request with parameters (simulasi - pakai httpbin.org)
print("\n#3: Request with Query Parameters (Simulated)")

params = {
    "province_id": "32",  # Simulasi: Jawa Barat
    "include": "cities"
}

try:
    response = requests.get("https://httpbin.org/get", params=params)
    print(f"✅ Status Code: {response.status_code}")
    data = response.json()
    print(f"✅ Final URL: {data['url']}")
    print(f"✅ Sent Parameters: {data['args']}")
except Exception as e:
    print(f"❌ Error with parameters: {e}")

# 💡 Summary
print("\n💡 Key Learning Points:")
print("- HTTP status codes: 200 (OK), 404 (Not Found), 500 (Server Error)")
print("- Headers provide additional information about the request")
print("- Query parameters are used to send data in the URL")
print("- Always handle exceptions for error handling")

