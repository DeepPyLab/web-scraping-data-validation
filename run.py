# run.py

from app.scraper import scrape_weather_data
from app.validator import validate_weather_data


def main():
    data = scrape_weather_data()

    if data:
        is_valid, message = validate_weather_data(data)
        print(message)
        if is_valid:
            print(f"Scraped Weather Data: {data}")
        else:
            print("Data validation failed.")
    else:
        print("Failed to scrape weather data.")


if __name__ == '__main__':
    main()
