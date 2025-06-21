import requests
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.parse
import csv
import xml.etree.ElementTree as ET

# =============================================================================
# STEP 2: WORKING WITH APIs - USING INDONESIAN APIs
# =============================================================================

def step2_working_with_apis():
    print("\n📚 STEP 2: WORKING WITH APIs")
    print("-" * 40)
    print("🎯 Objective: Accessing real-time data through APIs")
    print("📖 Concepts: REST API, JSON, Authentication, Rate Limiting")

    # 2.1 Indonesian Region API
    print("\n2.1 Accessing Indonesian Region API")
    try:
        url = 'https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json'
        headers = {"User-Agent": "LatihanAPI/1.0"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            provinces = response.json()
            print(f"✅ Retrieved {len(provinces)} provinces")
            print("✅ First 5 provinces:")
            for i, province in enumerate(provinces[:5]):
                print(f"   {i+1}. {province['name']}")
        else:
            print(f"❌ Error: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # 2.2 Weather API Simulation
    print("\n2.2 Jakarta Weather API Simulation")
    def get_simulated_weather(city="Jakarta"):
        return {
            "city": city,
            "temperature": 28.5,
            "humidity": 75,
            "condition": "Partly Cloudy",
            "wind_speed": 12.3,
            "timestamp": datetime.now().isoformat()
        }

    weather = get_simulated_weather("Jakarta")
    print(f"✅ Weather in {weather['city']}: {weather['temperature']}°C")
    print(f"✅ Condition: {weather['condition']}")
    print(f"✅ Humidity: {weather['humidity']}%")

    # 2.3 Error Handling
    print("\n2.3 Error Handling for API Calls")
    def safe_api_call(url, max_retries=3):
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"⚠️ Attempt {attempt + 1}: Status {response.status_code}")
            except requests.exceptions.Timeout:
                print(f"⚠️ Attempt {attempt + 1}: Timeout")
            except requests.exceptions.ConnectionError:
                print(f"⚠️ Attempt {attempt + 1}: Connection Error")
            time.sleep(2 ** attempt)
        return None

    result = safe_api_call('https://httpbin.org/delay/1')
    print("✅ Safe API call successful" if result else "❌ Safe API call failed")

    # 2.4 BMKG Earthquake Data (XML)
    print("\n2.4 Accessing Earthquake Data from BMKG (XML Format)")
    try:
        url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.xml"
        response = requests.get(url)
        root = ET.fromstring(response.content)
        earthquakes = root.findall(".//gempa")
        print(f"✅ Retrieved {len(earthquakes)} recent earthquakes")
        print("📌 Sample (first 3 events):")
        for i, g in enumerate(earthquakes[:3]):
            print(f"   {i+1}. {g.find('Tanggal').text} | {g.find('Wilayah').text} | M{g.find('Magnitude').text} | Depth: {g.find('Kedalaman').text}")
    except Exception as e:
        print(f"❌ Error fetching BMKG earthquake data: {e}")

    # 2.5 Currency Exchange Rate
    print("\n2.5 Accessing Currency Exchange API (USD to IDR)")
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IDR"
        response = requests.get(url)
        rate = response.json()['rates']['IDR']
        print(f"✅ USD to IDR exchange rate: {rate}")
    except Exception as e:
        print(f"❌ Error fetching exchange rate: {e}")

    # 2.6 Fake Store Product Data
    print("\n2.6 Accessing Product Data (Fake Store API)")
    try:
        url = "https://fakestoreapi.com/products"
        response = requests.get(url)
        products = response.json()
        print(f"✅ Retrieved {len(products)} products")
        for item in products[:3]:
            print(f" - {item['title']} | ${item['price']}")
    except Exception as e:
        print(f"❌ Error fetching product data: {e}")

    # 2.7 COVID-19 Indonesia Historical Data
    print("\n2.7 COVID-19 Indonesia Historical Data")
    try:
        url = "https://api.kawalcorona.com/indonesia/"
        response = requests.get(url)
        data = response.json()[0]
        print(f"✅ Positif:   {data['positif']}")
        print(f"✅ Sembuh:    {data['sembuh']}")
        print(f"✅ Meninggal: {data['meninggal']}")
    except Exception as e:
        print(f"❌ Error fetching COVID data: {e}")

    # Summary
    print("\n💡 Key Learning Points:")
    print("- APIs return data in JSON or XML format")
    print("- Always check status code before processing data")
    print("- Implement retry mechanism for reliability")
    print("- Use timeout to avoid hanging requests")
    print("- XML APIs require parsing with ElementTree or BeautifulSoup")
    print("- Real-time data from trusted sources like BMKG can support public alerts")

# Jalankan
if __name__ == "__main__":
    step2_working_with_apis()
