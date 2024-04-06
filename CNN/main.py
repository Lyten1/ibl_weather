import requests


def fetch_and_print_temperature(url, params):

    # Send GET request to retrieve data
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON content from the response
        data = response.json()



        # Access to temperature measurements
        # Note: The keys used below ('temperature') should be replaced with the actual keys used by the API for temperature data
        temperature_measurements = data.get('ranges', {}).get('temperature', {}).get('values', [])

        # Access to coordinates and timestamps
        coordinates = data.get('domain', {}).get('axes', {}).get('composite', {}).get('values', [])
        time_stamps = data.get('domain', {}).get('axes', {}).get('t', {}).get('values', [])

        features = data.get('features', [])

        for feature in features:
            # Extracting coordinates
            coordinates = feature['geometry']['coordinates']

            # Extracting temperature measurement
            temperature = feature['properties']['measures'].get('temperature', {}).get('value', 'N/A')

            # Extracting time of temperature measurement
            time_of_measurement = feature['properties']['measures'].get('temperature', {}).get('time_of_measurement',
                                                                                               'N/A')

            print(f"Coordinates: {coordinates}, Temperature: {temperature}°C, Time of Measurement: {time_of_measurement}")

    else:
        # If the request fails, print the error message
        print(f"Error: {response.status_code} - {response.reason}")

# Example usage
url = "https://climathon.iblsoft.com/data/netatmo/edr/collections/publicdata/radius"
params = {
    "coords": "POINT(17.1785 48.1628)",
    "crs": "CRS:84",
    "within": "2",
    "within-units": "km",
    "datetime": "2023-10-15T06:20:00Z"  # Example datetime parameter
}




# Fetch and print temperature based on the specified query
fetch_and_print_temperature(url, params)

