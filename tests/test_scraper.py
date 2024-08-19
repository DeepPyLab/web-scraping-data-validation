# tests/test_scraper.py

import unittest
from app.scraper import fetch_html, parse_data, scrape_data

class TestScraper(unittest.TestCase):

    def test_fetch_html_success(self):
        # Replace with a URL known to work in tests
        url = 'https://example.com'
        html_content = fetch_html(url)
        self.assertIsNotNone(html_content)

    def test_fetch_html_failure(self):
        url = 'https://nonexistenturl.com'
        html_content = fetch_html(url)
        self.assertIsNone(html_content)

    def test_parse_data(self):
        html_content = "<html><head><title>Test Page</title></head><body></body></html>"
        data = parse_data(html_content)
        self.assertEqual(data['title'], 'Test Page')

    def test_scrape_data(self):
        url = 'https://example.com'
        data = scrape_data(url)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
