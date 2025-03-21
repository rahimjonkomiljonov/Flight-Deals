# Flight Price Tracker

A Python script that monitors flight prices from a specified origin city to multiple destinations and sends SMS notifications when prices drop below set thresholds.

## Features
- Tracks flight prices from a single origin to multiple destinations
- Checks prices for the next 6 months
- Sends SMS notifications for low-price alerts
- Integrates with Sheety for destination data management
- Handles rate limiting with request delays

## Prerequisites
- Python 3.x
- Required Python packages:
  - `requests` (implied for API calls)
  - Custom classes:
    - `data_manager.py` (Sheety_Manager)
    - `flight_search.py` (FlightSearch)
    - `flight_data.py` (find_cheapest_flight)
    - `notification_manager.py` (NotificationManager)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/flight-price-tracker.git
cd flight-price-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up required external services:
- Sheety account for destination data
- Flight search API (implementation dependent)
- SMS service (e.g., Twilio) for notifications

## Configuration
- `ORIGIN_CITY_IATA`: Set to "ICN" (Incheon International Airport) by default
- Destination data stored in Sheety spreadsheet with columns:
  - `city`: Destination city name
  - `iataCode`: Destination airport IATA code
  - `lowestPrice`: Target price threshold
- Configure API keys/credentials in respective class files

## Usage
1. Ensure all class dependencies are properly configured
2. Run the script:
```bash
python flight_tracker.py
```

## How It Works
1. Retrieves destination data from Sheety
2. For each destination:
   - Searches flights from origin (ICN) to destination
   - Checks prices for next 6 months
   - Finds cheapest available flight
   - Compares with target price
   - Sends SMS if price is lower than threshold
3. Implements 2-second delay between requests to avoid rate limiting

## File Structure
- `flight_tracker.py`: Main script
- `data_manager.py`: Sheety data management
- `flight_search.py`: Flight search API integration
- `flight_data.py`: Flight data processing
- `notification_manager.py`: SMS notification handling

## Notes
- Searches flights from tomorrow to 6 months ahead
- Uses IATA codes for airports
- Price is displayed in GBP (£)
- Requires separate implementation of supporting classes
- Includes basic rate limiting with 2-second sleep

## Dependencies
```bash
# Suggested requirements.txt
requests
# Add any additional dependencies required by the custom classes
```

## Customization
- Change `ORIGIN_CITY_IATA` to your preferred departure airport
- Modify date range by adjusting `timedelta` values
- Adjust sleep time based on API rate limits
- Update currency display in notification message

## Limitations
- Dependent on external API availability
- Requires separate implementation of supporting classes
- Basic error handling not shown in main script

## License
[MIT License](LICENSE)

## Disclaimer
Ensure compliance with:
- Flight search API terms of service
- SMS service provider regulations
- Sheety usage policies
```
