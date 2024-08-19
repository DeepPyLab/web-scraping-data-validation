# app/validator.py

def validate_weather_data(data):
    """Validate the scraped weather data."""
    if not data:
        return False, "No data provided"

    # Example validation: Check if temperature is present
    temperature = data.get('temperature', '')

    if 'No temperature data found' in temperature:
        return False, "Temperature data is missing"

    # More validation checks can be added here
    return True, "Weather data is valid"
