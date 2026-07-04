# Validation Checks

## After Step 3 (hub created)
The deployment overview should read "Your deployment is complete" with exactly four resources listed, all status **OK**:
- your hub name (type: Microsoft.MachineLearningServices)
- `<hubname><random>` (type: Microsoft.CognitiveServices/accounts)
- `<hubname><random>` (type: Storage account)
- `<hubname><random>` (type: Key vault)

If any show a status other than OK, check `05-troubleshooting.md` before proceeding.

## After Step 4 (project created)
You should land on the project's Overview page in ai.azure.com without an error, showing "Endpoints and keys" and "Project details" panels, and the Project name in the top-right matching what you entered in the "Name your project" dialog.

## After Step 6 (RBAC located)
"View my access" on the hub's Access control (IAM) page should return at least one role (commonly Owner or Contributor, depending on how the resource was created).

## After Step 7 (Management center and nav groups located)
You should be able to name the three project-level navigation groups (Build and customize, Observe and optimize, Protect and govern) and know that hub-level fleet visibility lives in the Management center, not a project tab.

If any step fails to load or shows an access error, go to `05-troubleshooting.md`.
