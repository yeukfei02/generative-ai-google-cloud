# generative-ai-google-cloud

generative-ai-google-cloud

documentation: <>

findAddress api url: <>

getCheapFood api url: <>

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
