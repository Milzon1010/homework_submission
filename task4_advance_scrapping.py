# =============================================================================
# STEP 4: ADVANCED SCRAPING TECHNIQUES
# =============================================================================
import requests
import time
from bs4 import BeautifulSoup

print("\n📚 STEP 4: ADVANCED SCRAPING TECHNIQUES")
print("-" * 40)

def step4_advanced_scraping():
    """
    Step 4: Advanced scraping techniques for Indonesian railway schedules
    """
    print("🎯 Objective: Scrape transport data from dynamic web pages")
    print("📖 Concepts: Session usage, rate limiting, headers, structured scraping")
    
    # Example 1: Using Sessions
    print("\n4.1 Using Sessions for Scraping")
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8',
        'Referer': 'https://kai.id',
        'Connection': 'keep-alive'
    })
    
    print("✅ Session created with realistic headers")
    print(f"✅ Using Referer: {session.headers['Referer']}")
    
    # Example 2: Rate Limiting
    print("\n4.2 Rate Limiting Implementation")
    
    class TrainScraper:
        def __init__(self, delay=1.5):
            self.delay = delay
            self.last_request = 0
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Train-Scraper-Bot/1.0 (Learning Purpose Only)'
            })
        
        def get_page(self, url):
            elapsed = time.time() - self.last_request
            if elapsed < self.delay:
                wait = self.delay - elapsed
                print(f"⏳ Waiting {wait:.1f} seconds before next request...")
                time.sleep(wait)
            try:
                response = self.session.get(url)
                self.last_request = time.time()
                return response
            except Exception as e:
                print(f"❌ Error: {e}")
                return None
    
    train_scraper = TrainScraper(delay=1.5)
    print("✅ Train scraper with rate limiting initialized")
    
    # Example 3: Handling Schedule Table (simulated HTML)
    print("\n4.3 Parsing Simulated Train Schedule Data")
    
    def extract_train_schedule(html):
        soup = BeautifulSoup(html, 'html.parser')
        # Simulated extraction (in practice, parse real table structure)
        schedule = [
            {
                'train': 'Argo Parahyangan',
                'departure': '07:15',
                'arrival': '11:30',
                'from': 'Bandung',
                'to': 'Gambir'
            },
            {
                'train': 'Taksaka Pagi',
                'departure': '08:00',
                'arrival': '14:15',
                'from': 'Yogyakarta',
                'to': 'Gambir'
            }
        ]
        return schedule
    
    sample_html_schedule = "<html><body>Simulated train schedule data</body></html>"
    schedule = extract_train_schedule(sample_html_schedule)
    
    print(f"✅ Extracted {len(schedule)} train entries:")
    for trip in schedule:
        print(f"   🚆 {trip['train']}")
        print(f"      🕗 {trip['departure']} → {trip['arrival']}")
        print(f"      📍 From: {trip['from']} → To: {trip['to']}")
    
    print("\n💡 Key Learning Points:")
    print("- Simulate sessions and headers to mimic real users")
    print("- Always wait between requests to avoid bans")
    print("- Structure your scraping functions to be reusable")
    print("- Simulated data is a safe way to test logic before scraping real sites")

if __name__ == "__main__":
    step4_advanced_scraping()


    