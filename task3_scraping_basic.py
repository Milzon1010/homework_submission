
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

# =============================================================================
# STEP 3: INTRODUCTION TO WEB SCRAPING
# =============================================================================

print("\n📚 STEP 3: INTRODUCTION TO WEB SCRAPING")
print("-" * 40)

def step3_web_scraping_basics():
    """
    Step 3: Web scraping basics with BeautifulSoup - Weather Report Example
    """
    print("🎯 Objective: Extracting weather data from web pages")
    print("📖 Concepts: HTML parsing, CSS selectors, BeautifulSoup")
    
    # Example 1: Simple HTML parsing
    print("\n3.1 Simple HTML Parsing")
    sample_html = """
    <html>
        <head><title>Today's Weather</title></head>
        <body>
            <h1>City Weather Report</h1>
            <div class="weather-container">
                <div class="weather-item">
                    <h2>Jakarta</h2>
                    <p class="temp">Temperature: 32°C</p>
                    <span class="status">Sunny</span>
                </div>
                <div class="weather-item">
                    <h2>Bandung</h2>
                    <p class="temp">Temperature: 24°C</p>
                    <span class="status">Cloudy</span>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    # Extract title
    title = soup.find('title').text
    print(f"✅ Page title: {title}")
    
    # Extract all weather items
    weather_items = soup.find_all('div', class_='weather-item')
    print(f"✅ Found {len(weather_items)} city weather reports:")
    
    for i, item in enumerate(weather_items, 1):
        city = item.find('h2').text
        temperature = item.find('p', class_='temp').text
        status = item.find('span', class_='status').text
        print(f"   {i}. {city}")
        print(f"      {temperature}")
        print(f"      Status: {status}")
    
    # Example 2: CSS Selectors
    print("\n3.2 Using CSS Selectors")
    
    # Select by class
    temps = soup.select('.temp')
    print(f"✅ Temperatures using CSS selector:")
    for i, temp in enumerate(temps, 1):
        print(f"   {i}. {temp.text}")
    
    # Select by tag and class
    statuses = soup.select('span.status')
    print(f"✅ Weather statuses: {[s.text for s in statuses]}")
    
    # Example 3: Scraping with requests + BeautifulSoup
    print("\n3.3 Real Web Scraping (Simulation)")
    
    def scrape_weather_simulation():
        """Simulated scraping for weather reports"""
        weather_data = [
            {
                "city": "Surabaya",
                "temperature": "35°C",
                "status": "Sunny"
            },
            {
                "city": "Yogyakarta",
                "temperature": "29°C",
                "status": "Rainy"
            },
            {
                "city": "Medan",
                "temperature": "30°C",
                "status": "Thunderstorm"
            }
        ]
        return weather_data
    
    reports = scrape_weather_simulation()
    print(f"✅ Successfully scraped {len(reports)} weather entries:")
    for i, report in enumerate(reports, 1):
        print(f"   {i}. {report['city']}")
        print(f"      Temperature: {report['temperature']}")
        print(f"      Status: {report['status']}")
    
    print("\n💡 Key Learning Points:")
    print("- BeautifulSoup helps extract data from HTML")
    print("- Use find() and find_all() to locate HTML elements")
    print("- CSS selectors allow flexible element targeting")
    print("- Simulated data can be used for offline practice")

if __name__ == "__main__":
    step3_web_scraping_basics()
    