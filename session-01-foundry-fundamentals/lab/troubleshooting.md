# Troubleshooting

## Can't create a hub — "insufficient permissions"
You need at least Contributor role on the subscription or target resource group. Ask your subscription admin to grant this, or use a sandbox/personal subscription for learning.

## Project creation fails silently
Refresh the portal — occasionally the hub takes a few seconds to fully provision before it will accept a new project. Wait 30 seconds and retry.

## RBAC blade shows no roles
This can mean roles are assigned at a higher scope (management group or subscription level) rather than directly on the hub. Check subscription-level IAM if the hub-level blade looks empty.

## Operate tab is missing or greyed out
This feature may be region-dependent or still rolling out to some tenants. If it's not visible, note it and continue — we revisit this in Session 7 with more specific setup steps.
