# Architecture & Flow

## Where deployment sits

Deployment happens from a model's card in the catalog (a "Deploy" action) or from a dedicated Deployments section in the project — both should be confirmed against the actual portal layout, since this wasn't verified during scaffolding.

## The deployment decision flow

```
Shortlisted model (from Session 2)
    -> Confirm deployment types available for this specific model
    -> Confirm quota available in your target region
    -> Choose: Standard / Provisioned throughput / Serverless API
    -> Deploy
    -> Test in Playground with your own prompts
    -> Decide: keep running, or clean up
```

## Where Model Router fits

Model Router is a distinct deployment option, not a modifier applied on top of a single-model deployment. Conceptually:

```
Standard single-model deployment:
    Your app -> one fixed model -> response

Model Router deployment:
    Your app -> router -> (picks one of several underlying models per request) -> response
```

