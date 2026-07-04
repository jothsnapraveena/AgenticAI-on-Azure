# Cleanup

## Delete the hub — this cascades automatically
Deleting the hub directly removes it and its associated resources in one action. From the hub's overview page (or from the Management center), select **Delete hub**.

You'll see a "Delete resource status" screen listing each associated resource as it's removed, typically including:
- the AI Hub itself
- the AI Project created inside it
- the Storage account
- the Key Vault

Each shows status **Accepted** while deletion is in progress. You do not need to delete the project separately first, and you do not need to delete the resource group as a workaround — deleting the hub handles the cascade.

## If the Cognitive Services account remains
The Cognitive Services account created alongside the hub (the one backing model access) is not always included in the hub's cascade delete. Check the resource group afterward — if it's still there and you don't need it, delete it separately from the resource group view.

## Confirm deletion
Return to the Azure portal's resource groups list. If nothing else was in that resource group, it should now be empty or show only the Cognitive Services account if that one wasn't cascade-deleted.
