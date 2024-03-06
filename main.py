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

            result += response.text.replace('\n', '<br/>')

    return result
