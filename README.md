# generative-ai-google-cloud

This project intends to use google cloud function with vertex ai gemini to make API with generative ai, there are two API for `text-to-text` and `text-to-image`

The model uses `gemini 1.0` and `imagen 005`

documentation: <https://documenter.getpostman.com/view/3827865/2sA2xe6FP5>

getItinerary api url: <https://asia-southeast1-strange-vortex-416210.cloudfunctions.net/generative-ai-gcloud-prod>

generate wallpaper api url: <https://asia-southeast1-strange-vortex-416210.cloudfunctions.net/generative-ai-gcloud-prod>

travel planner web url: <https://travel-planner-gen-ai.streamlit.app/>

generate wallpaper web url: <https://generate-wallpaper.streamlit.app/>

## Requirement

- install yarn
- install node (v18)
- install python (v3.9)
- install serverless
- install gcloud cli

## Testing and run

```zsh
// get bearer token
$ gcloud auth print-identity-token

// deploy to serverless
$ yarn run deploy

// generate .serverless folder
$ yarn run package

// remove serverless services in google cloud
$ yarn run remove

// check serverless.yml
$ yarn run doctor
```

```zsh
// install dependencies
$ cd web
$ pip install -r requirements.txt

// open web
$ streamlit run travel_planner.py
```
