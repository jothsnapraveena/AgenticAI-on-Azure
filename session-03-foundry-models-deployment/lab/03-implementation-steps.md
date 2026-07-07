# Implementation Steps

**Note:** This is a first-pass draft based on general Foundry deployment concepts, not yet verified against the live portal. Every step here should be checked against what you actually see and corrected before this file is considered final.

## 1. Open your shortlisted model's card

From the Model catalog, open the model card for your Session 2 primary choice.

## 2. Start the deploy flow

Look for a "Deploy" or "Use this model" action on the model card.

## 3. Choose a deployment type

Select from whatever deployment types the model card shows as available for that model (Standard, Provisioned throughput, or Serverless API). Confirm the region matches where you have quota.

## 4. Name and confirm the deployment

Give the deployment a name you'll recognize later, confirm the configuration, and deploy.

## 5. Wait for the deployment to go live

Deployments typically take a short time to provision — confirm the actual wait time and any status indicators shown in the portal.

## 6. Test in the Playground

Open Playgrounds, select your new deployment, and run a few prompts representative of your actual task (the one you picked back in Session 2's prerequisites).

## 7. (Optional) Try Model Router

If you want to compare, repeat steps 2-6 choosing Model Router instead of your single model, and see whether the portal exposes which underlying model answered each prompt.

## 8. Record your results

Note response quality, latency, and anything surprising for `07-proof-of-execution.md`.
