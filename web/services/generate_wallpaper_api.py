import requests


def generate_wallpaper_api(text, image_count, token):
    result = None

    try:
        root_url = "https://asia-southeast1-strange-vortex-416210.cloudfunctions.net/generative-ai-gcloud-prod-generateWallpaper"

        params = {
            "text": text,
            "image_count": image_count
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(root_url, params=params, headers=headers)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json["result"]
    except Exception as e:
        print(f"generate_wallpaper_api error = {e}")

    return result
