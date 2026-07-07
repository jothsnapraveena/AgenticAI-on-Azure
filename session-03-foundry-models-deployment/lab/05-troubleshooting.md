# Troubleshooting

**Deployment fails with a quota error.**
Your subscription/region combination doesn't have enough quota for that model. Either request a quota increase, pick a different region with available quota, or choose a smaller model variant if one exists.

**The model I want to deploy doesn't show a "Deploy" option.**
Some models are catalog-listed but require an application/access request before deployment (common for certain frontier or gated models). Check the model card for any access requirements.

**Playground doesn't show my new deployment.**
Deployments can take a short time to fully propagate. Refresh, and confirm you're looking at the right project if you have more than one.

**Model Router responses seem inconsistent between runs.**
This may be expected behavior — different requests can be routed to different underlying models. Confirm whether the portal or API response surfaces which model actually answered, so you can attribute the inconsistency correctly rather than assuming it's an error.
