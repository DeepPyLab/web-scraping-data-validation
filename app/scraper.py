import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    """Fetch the HTML content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_weather_data(html_content):
    """Parse the HTML content and extract the current temperature."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Extracting the temperature
    temp_element = soup.find('span', class_='CurrentConditions--tempValue--MHmYY')

    if temp_element:
        temperature = temp_element.text
        return {'temperature': temperature}
    else:
        # Output the HTML to troubleshoot if data is missing
        with open('debug.html', 'w', encoding='utf-8') as file:
            file.write(str(soup.prettify()))
        return {'temperature': 'No temperature data found'}


def scrape_weather_data():
    """Main function to scrape weather data for New York City."""
    # Use the specific URL for New York City on Weather.com
    url = "https://weather.com/weather/today/l/USNY0996:1:US"  # New York City location key
    html_content = fetch_html(url)
    if html_content:
        return parse_weather_data(html_content)
    return None
