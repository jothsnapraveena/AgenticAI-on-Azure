# Cleanup

Unlike Session 2, this session provisions a real, billable deployment. Do not skip this step.

## Steps (to be confirmed against the live portal)

1. Go to the Deployments section of your Foundry project
2. Locate the deployment(s) you created in this session (including any Model Router deployment from step 7)
3. Delete each deployment
4. Confirm deletion — check that the deployment no longer appears in the list
5. If you created any new quota requests or resources specifically for this session, note whether those also need separate cleanup

## Why this matters

Provisioned throughput deployments in particular can carry a meaningful ongoing cost even with zero traffic, since you're paying for reserved capacity rather than per-token usage. Even Standard deployments are worth deleting once you're done testing, to avoid an idle resource lingering in your subscription.
