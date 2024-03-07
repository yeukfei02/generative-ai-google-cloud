import requests


def get_itinerary_api(day, country):
    result = None

    try:
        root_url = "https://asia-southeast1-strange-vortex-416210.cloudfunctions.net/generative-ai-gcloud-prod-getItinerary"

        params = {
            "day": day,
            "country": country
        }

        response = requests.get(root_url, params=params)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json["result"]
    except Exception as e:
        print(f"get_itinerary_api error = {e}")

    return result
