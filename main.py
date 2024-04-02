import requests
import vertexai
from vertexai.preview.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models


def get_itinerary_handler(request):
    print(f"request = {request}")

    response = {
        "message": "get_itinerary",
        "result": {}
    }

    day = request.args.get("day") or "5"
    country = request.args.get("country") or "Hong Kong"

    result = generate_itinerary_by_gemini(day, country)
    if result:
        response = {
            "message": "get_itinerary",
            "result": result
        }

    headers = {
        "Access-Control-Allow-Origin": "*"
    }

    return (response, 200, headers)


def generate_wallpaper_handler(request):
    print(f"request = {request}")

    response = {
        "message": "generate_wallpaper",
        "result": {}
    }

    text = request.args.get("text")
    image_count = request.args.get("image_count") or "1"
    token = request.args.get("token")

    if text and image_count and token:
        result = generate_wallpaper_by_imagen(text, image_count, token)
        if result:
            response = {
                "message": "generate_wallpaper",
                "result": result
            }

    headers = {
        "Access-Control-Allow-Origin": "*"
    }

    return (response, 200, headers)


def generate_itinerary_by_gemini(day, country):
    result = ""

    vertexai.init(project="strange-vortex-416210", location="asia-southeast1")

    model = GenerativeModel("gemini-1.0-pro-001")

    responses = model.generate_content(
        f"""
            Generate a {day}-day itinerary for a trip to {country}.
            Show attractions, food places and restaurants with the price, location, opening hours, contact information, and website.
        """,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.3,
            "top_p": 1
        },
        safety_settings={
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=True,
    )
    print(f"responses = {responses}")

    if responses:
        for response in responses:
            print(f"response.text = {response.text}")

            result += response.text

    return result


def generate_wallpaper_by_imagen(text, image_count, token):
    result = None

    try:
        project_id = "672765669230"
        region = "asia-southeast1"

        root_url = f"https://{region}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{region}/publishers/google/models/imagegeneration:predict"

        body = {
            "instances": [
                {
                    "prompt": text
                }
            ],
            "parameters": {
                "sampleCount": int(image_count)
            }
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.post(root_url, json=body, headers=headers)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json["predictions"]
    except Exception as e:
        print(f"generate_wallpaper_by_imagen error = {e}")

    return result
